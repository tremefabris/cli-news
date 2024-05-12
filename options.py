import argparse
from utils import COLOR

def get_options():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--jornal", "-j", type=str, required=True,
                        help="Qual jornal acessar: G1, NEXO, JAV",
                        metavar="STR")
    
    parser.add_argument("--color", "-c", type=str, required=False,
                        default="blue",
                        help="Cor usada para o nome do jornal: {0}RED{3}, {1}GREEN{3}, {2}BLUE{3}".format(
                            COLOR["RED"], COLOR["GRN"], COLOR["BLU"], COLOR["RST"]
                        ),
                        metavar="STR")

    return parser.parse_args()