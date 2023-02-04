r"""
This module contains the :class: `PotentialReference` which contains every to with reference
potentials. 
"""
# ********************************************************************
#  This file is part of svgdigitizer.
#
#        Copyright (C) 2022 Johannes Hermann
#
#  svgdigitizer is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  svgdigitizer is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with svgdigitizer. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************
from astropy import units as u


class PotentialReference:
    r"""
    :class: PotentialReference models the electrolyte i.e. the solution with all it's components.
    EXAMPLES:
    >>> from svgdigitizer.electrochemistry.potential_reference import PotentialReference
    >>> potential_reference = PotentialReference("MSE-sat")

    """
    # Data take from:
    # Inzelt, G., Lewenstam, A., Scholz, F. (Eds.), 2013. Handbook of Reference Electrodes. 
    # Springer Berlin Heidelberg, Berlin, Heidelberg. https://doi.org/10.1007/978-3-642-36188-3
     
    references = { "Ag/AgCl-sat": {"E(T)": lambda T: 0.23659 - 4.8564e-4 * T - 3.4205e-6 * T**2 + 5.869e-9 * T**3},
        "SCE-sat": {"E(T)": lambda T: 0.2412 - 6.61e-4*(T-25) - 1.75e-6*(T-25)**2 - 9e-10*(T-25)**3},
        "MSE-1M": {"E(T)": lambda T: 0.63495 - 781.44e-6*T - 426.89e-9*T**2},
        "SHE": {"E(T)": lambda T: 0}

    }

    def __init__(self, reference, T = 25, pH = None):
        self.reference = reference
        self.T = T
        self.pH = pH
    
    def to_reference(self, new_reference):
        """ TESTS:
        >>> from svgdigitizer.electrochemistry.potential_reference import PotentialReference
        >>> potential_reference = PotentialReference("MSE-1M")
        >>> potential_reference.to_reference("SCE-sat")
        -0.3739471937500001
        >>> potential_reference.to_reference("SHE")
        -0.61514719375
        """
        return self.references[new_reference]["E(T)"](self.T) - self.references[self.reference]["E(T)"](self.T)
