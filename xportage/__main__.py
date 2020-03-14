# __main__.py

import argparse
import os

from xportage import xportage as xp

HOME = os.path.expanduser('~')


def main(options):
    xph = xp.XPortageHome(options.home, options.cfg, force=options.force)
    xph.print_configuration()
    xph.print_summary()

    if options.download is not None:
        xph.download(ref_name=options.download)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('home', type=str, help='Path to XPORTAGE_HOME.')
    parser.add_argument('--cfg', default=os.path.join(HOME, '.xportage', 'cfg.json'), type=str, help='Path to XPORTAGE_CFG.')
    parser.add_argument('--force', action='store_true', help='If True, then always reset config.')
    parser.add_argument('--download', default=None, type=str, help='If set, then will download dataset using reference info.')
    options = parser.parse_args()

    main(options)
