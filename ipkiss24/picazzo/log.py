# IPKISS - Parametric Design Framework
# Copyright (C) 2002-2012  Ghent University - imec
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# i-depot BBIE 7396, 7556, 7748
#
# Contact: ipkiss@intec.ugent.be

__all__ = ["PICAZZO_LOG"]

import logging
import sys

PICAZZO_LOGGING_HANDLER = logging.StreamHandler(sys.stderr)
PICAZZO_LOG = logging.getLogger('PICAZZO')
PICAZZO_LOG.setLevel(logging.ERROR)
PICAZZO_LOG.addHandler(PICAZZO_LOGGING_HANDLER)