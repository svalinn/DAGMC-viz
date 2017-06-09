# Adds terminal execution. This is still a work in progress.
parser = argparse.ArgumentParser(
    description = 'Terminal execution of tool.',
    usage = 'Remains to be seen.',
    )
parser.add_argument('file')
parser.add_argument('plot')
parser.add_argument('vari')
args = parser.parser_args()

self.file = args.file
self.plot = args.plot
self.vari = args.vari