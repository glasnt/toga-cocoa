# Core capabilities
from .app import *
from .window import *
from .command import *

# Widgets
from .widgets.button import *
from .widgets.container import *
from .widgets.icon import *
from .widgets.label import *
from .widgets.dialog import *
from .widgets.multilinetextinput import *
from .widgets.optioncontainer import *
from .widgets.passwordinput import *
from .widgets.progressbar import *
from .widgets.scrollcontainer import *
from .widgets.splitcontainer import *
from .widgets.table import *
from .widgets.textinput import *
from .widgets.tree import *
from .widgets.webview import *

__all__ = [
    '__version__',
    'App',
    'Window',
    'Command', 'SEPARATOR', 'SPACER', 'EXPANDING_SPACER',
    'Button',
    'Container',
    'Icon', 'TIBERIUS_ICON',
    'Label',
    'Dialog',
    'MultilineTextInput',
    'OptionContainer',
    'PasswordInput',
    'ProgressBar',
    'ScrollContainer',
    'SplitContainer',
    'Table',
    'TextInput',
    'Tree',
    'WebView',
]

# Examples of valid version strings
# __version__ = '1.2.3.dev1'  # Development release 1
# __version__ = '1.2.3a1'     # Alpha Release 1
# __version__ = '1.2.3b1'     # Beta Release 1
# __version__ = '1.2.3rc1'    # RC Release 1
# __version__ = '1.2.3'       # Final Release
# __version__ = '1.2.3.post1' # Post Release 1

__version__ = '0.1.3.dev'

# Toga uses the autolayout features introduced in
# OS X 10.7 (Lion). Earlier versions won't work.
import platform

if tuple(int(v) for v in platform.mac_ver()[0].split('.')[:2]) < (10, 7):
    raise RuntimeError('Toga requires OS X 10.7 (Lion) or greater.')
