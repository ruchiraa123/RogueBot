from constants import *

name = 'Белок зелье'

description = (
	'Пробирка с каким-то серым зельем'
)

price = 100
usable = True
disposable = True

def on_use(user, reply):
	reply('Теперь ты Булыжник.', [ ])

	user.reborn(reply, 'Булыжник должен лежать', photo='BQADAgAD8gADDLXzAxLUH2ng6NIiAg')
