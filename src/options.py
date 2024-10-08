import argparse
from .color import Color as C

def get_options():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--jornal", "-j", type=str, required=True,
                        help="Qual jornal acessar: G1, NEXO, JAV",
                        metavar="STR")
    
    parser.add_argument("--color", "-c", type=str, required=False,
                        default="blue",
                        help="Cor usada para o nome do jornal: {0}, {1}, {2}".format(
                            C.red("RED"), C.green("GREEN"), C.blue("BLUE")),
                        metavar="STR")

    parser.add_argument("--since", '-s', type=int, required=False,
                        default=-1,
                        help="Pegar apenas matérias lançadas desde N dias atrás",
                        metavar="N")

    return parser.parse_args()