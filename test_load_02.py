import veusz.embed as veusz
import time

import logging

logging.basicConfig(level=logging.INFO)

#  open a new window and return a new Embedded object
embed = veusz.Embedded('window title')
embed.EnableToolbar()
embed.Load('s.vsz')
embed.ImportFileCSV('FiveBallAutoP_20220325-153933.csv', linked=True)
embed.SetDataExpression('turret.error', '`turret.position`-`turret.requested`', linked=True)

embed.WaitForClose()
