import typer
from ssg.Site import Site

def main(source="content",dest="dist"):
    config = {"source":source, "dest":dest}
    Site(**config).build()

typer.run(main)