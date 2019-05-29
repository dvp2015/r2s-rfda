# -*- coding: utf-8 -*-

import re
from pkg_resources import resource_filename
import numpy as np


def read_template(temp_name):
    with open(resource_filename(__name__, 'templates/' + temp_name)) as f:
        template = f.read()
    return template


files_temp = read_template('files.temp')
collapse_temp = read_template('collapse.temp')
condense_temp = read_template('condense.temp')
inventory_temp = None
flux_coeffs = None


def create_scenario_template(input):
    """Creates new template with replaced fluxes in irradiation scenario.

    New template is stored in module local variable since the template will not
    be changed for particular task.

    Parameters
    ----------
    input : str
        Input template of inventory input file.
    """
    global inventory_temp
    global flux_coeffs
    raise NotImplementedError


def fispact_files(datalib):
    """Creates files text.

    Parameters
    ----------
    datalib : str
        Text of data libraries.
    
    Returns
    -------
    text : str
        Text of files file.
    """
    raise NotImplementedError


def fispact_collapse(libxs, nestrc):
    """Creates collapse input file.

    Parameters
    ----------
    libxs : int
        If -1 - to use binary library, if +1 - use text library.
    nestrc : int
        The number of energy groups in neutron spectrum.
    
    Returns
    -------
    text : str
        Text of collapse file.
    """
    raise NotImplementedError


def fispact_inventory(flux):
    pass


def create_fispact_input(name, cwd, template, *args, **kwargs):
    """Creates fispact input file from the template.

    Parameters
    ----------
    name : str
        Name of FISPACT input file to be created.
    cwd : Path
        Working directory. In this directory files will be created. The folder
        must exist.
    template : str
        Template string with format specifiers. 
    *args : list
        A list of positional symbols that are to be inserted into template.
    **kwargs : dict
        A dictionary of named symbols that are to be inserted into template.
    """
    text = template.format(*args, **kwargs)
    with open(cwd / name, mode='w') as f:
        f.write(text)


def create_arbflux_text(ebins, flux):
    """Creates file for fispact flux conversion to the 709 groups.

    Parameters
    ----------
    ebins : array_like[float]
        Energy bins in MeV.
    flux : array_like[float]
        Group flux.

    Returns
    -------
    arb_flux : str
        Text for arb_flux file.
    """
    ncols = 6
    text = []
    for i, e in enumerate(reversed(ebins)):
        s = '\n' if (i + 1) % ncols == 0 else ' '
        text.append('{0:.6e}'.format(e * 1.e+6))  # Because fispact needs
        text.append(s)                            # eV, not MeV
    text[-1] = '\n'
   
    for i, e in enumerate(reversed(flux)):
        s = '\n' if (i + 1) % ncols == 0 else ' '
        text.append('{0:.6e}'.format(e))
        text.append(s)
    text[-1] = '\n'
    text.append('1\n')
    text.append('total flux={0:.6e}'.format(np.sum(flux)))

    return ''.join(text)
