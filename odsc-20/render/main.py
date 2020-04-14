import click
from jinja2 import Environment, FileSystemLoader, select_autoescape
import sys
import io
from contextlib import redirect_stdout
import textwrap
import inspect
import analysis

def trim_func(func_string):
    return(textwrap.dedent('\n'.join([
        x for x in func_string.strip().split('\n')
        if not x.strip().startswith('def') and not x.strip().startswith('return')
    ])))


def print_func(func):
    return(
        '```python\n{}\n```\n'
        .format(
            trim_func(inspect.getsource(func))
        )
    )


def capture_stdout(func):
    with io.StringIO() as stream:
        with redirect_stdout(stream):
            func()

        out = stream.getvalue()

    return(
        '\n'.join([
            '> ' + x
            for x
            in out.strip().split('\n')
        ])
    )


def print_and_run(func):
    return(
        '```python\n{}\n```\n```\nOutput: \n{}\n```\n'
        .format(
            trim_func(inspect.getsource(func)),
            capture_stdout(func)
        )
    )


def save_fig(plot, name):
    path = f'output/static/{name}.png'
    plot.save(path)

    return(path)


def print_and_plot(func, name):
    code = trim_func(inspect.getsource(func))
    path = save_fig(func(), name)

    return(
        '```python\n{}\n```\n![{}]({})\n\ \n'
        .format(code, name, path)
    )


@click.group()
def cli():
    pass


@cli.command()
def render():
    env = Environment(
        loader=FileSystemLoader('markdown/'),
        autoescape=select_autoescape()
    )
    env.filters['print_and_plot'] = print_and_plot
    env.filters['print_and_run'] = print_and_run
    env.filters['print_func'] = print_func

    template = env.get_template('bootstrap_breaks.md')

    with open('output/rendered.md', 'w') as outfile:
        outfile.write(template.render(analysis=analysis))


if __name__ == "__main__":
    render()

