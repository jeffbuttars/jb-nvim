from msg import ReqMsg
from cmds import Cmd


class Window(Cmd):

    def __init__(self, session):
        self._session = session

    # Function: window_get_buffer
    # Parameters Window: window
    # Returns Buffer
    # Recieves channel id False
    # Can fail True
    def get_buffer(self, window):
        return self.send_sync(ReqMsg('window_get_buffer', *[window]))

    # Function: window_get_cursor
    # Parameters Window: window
    # Returns ArrayOf(Integer, 2)
    # Recieves channel id False
    # Can fail True
    def get_cursor(self, window):
        return self.send_sync(ReqMsg('window_get_cursor', *[window]))

    # Function: window_set_cursor
    # Parameters Window: window, ArrayOf(Integer, 2): pos
    # Returns void
    # Recieves channel id False
    # Can fail True
    def set_cursor(self, window, pos):
        return self.send_sync(ReqMsg('window_set_cursor', *[window, pos]))

    # Function: window_get_height
    # Parameters Window: window
    # Returns Integer
    # Recieves channel id False
    # Can fail True
    def get_height(self, window):
        return self.send_sync(ReqMsg('window_get_height', *[window]))

    # Function: window_set_height
    # Parameters Window: window, Integer: height
    # Returns void
    # Recieves channel id False
    # Can fail True
    def set_height(self, window, height):
        return self.send_sync(ReqMsg('window_set_height', *[window, height]))

    # Function: window_get_width
    # Parameters Window: window
    # Returns Integer
    # Recieves channel id False
    # Can fail True
    def get_width(self, window):
        return self.send_sync(ReqMsg('window_get_width', *[window]))

    # Function: window_set_width
    # Parameters Window: window, Integer: width
    # Returns void
    # Recieves channel id False
    # Can fail True
    def set_width(self, window, width):
        return self.send_sync(ReqMsg('window_set_width', *[window, width]))

    # Function: window_get_var
    # Parameters Window: window, String: name
    # Returns Object
    # Recieves channel id False
    # Can fail True
    def get_var(self, window, name):
        return self.send_sync(ReqMsg('window_get_var', *[window, name]))

    # Function: window_set_var
    # Parameters Window: window, String: name, Object: value
    # Returns Object
    # Recieves channel id False
    # Can fail True
    def set_var(self, window, name, value):
        return self.send_sync(ReqMsg('window_set_var', *[window, name, value]))

    # Function: window_get_option
    # Parameters Window: window, String: name
    # Returns Object
    # Recieves channel id False
    # Can fail True
    def get_option(self, window, name):
        return self.send_sync(ReqMsg('window_get_option', *[window, name]))

    # Function: window_set_option
    # Parameters Window: window, String: name, Object: value
    # Returns void
    # Recieves channel id False
    # Can fail True
    def set_option(self, window, name, value):
        return self.send_sync(ReqMsg('window_set_option', *[window, name, value]))

    # Function: window_get_position
    # Parameters Window: window
    # Returns ArrayOf(Integer, 2)
    # Recieves channel id False
    # Can fail True
    def get_position(self, window):
        return self.send_sync(ReqMsg('window_get_position', *[window]))

    # Function: window_get_tabpage
    # Parameters Window: window
    # Returns Tabpage
    # Recieves channel id False
    # Can fail True
    def get_tabpage(self, window):
        return self.send_sync(ReqMsg('window_get_tabpage', *[window]))

    # Function: window_is_valid
    # Parameters Window: window
    # Returns Boolean
    # Recieves channel id False
    # Can fail False
    def is_valid(self, window):
        return self.send_sync(ReqMsg('window_is_valid', *[window]))


class Buffer(Cmd):

    def __init__(self, session):
        self._session = session

    # Function: buffer_line_count
    # Parameters Buffer: buffer
    # Returns Integer
    # Recieves channel id False
    # Can fail True
    def line_count(self, buffer):
        return self.send_sync(ReqMsg('buffer_line_count', *[buffer]))

    # Function: buffer_get_line
    # Parameters Buffer: buffer, Integer: index
    # Returns String
    # Recieves channel id False
    # Can fail True
    def get_line(self, buffer, index):
        return self.send_sync(ReqMsg('buffer_get_line', *[buffer, index]))

    # Function: buffer_set_line
    # Parameters Buffer: buffer, Integer: index, String: line
    # Returns void
    # Recieves channel id False
    # Can fail True
    def set_line(self, buffer, index, line):
        return self.send_sync(ReqMsg('buffer_set_line', *[buffer, index, line]))

    # Function: buffer_del_line
    # Parameters Buffer: buffer, Integer: index
    # Returns void
    # Recieves channel id False
    # Can fail True
    def del_line(self, buffer, index):
        return self.send_sync(ReqMsg('buffer_del_line', *[buffer, index]))

    # Function: buffer_get_line_slice
    # Parameters Buffer: buffer, Integer: start, Integer: end, Boolean: include_start, Boolean: include_end
    # Returns ArrayOf(String)
    # Recieves channel id False
    # Can fail True
    def get_line_slice(self, buffer, start, end, include_start, include_end):
        return self.send_sync(ReqMsg('buffer_get_line_slice', *[buffer, start, end, include_start, include_end]))

    # Function: buffer_set_line_slice
    # Parameters Buffer: buffer, Integer: start, Integer: end, Boolean: include_start, Boolean: include_end, ArrayOf(String): replacement
    # Returns void
    # Recieves channel id False
    # Can fail True
    def set_line_slice(self, buffer, start, end, include_start, include_end, replacement):
        return self.send_sync(ReqMsg('buffer_set_line_slice', *[buffer, start, end, include_start, include_end, replacement]))

    # Function: buffer_get_var
    # Parameters Buffer: buffer, String: name
    # Returns Object
    # Recieves channel id False
    # Can fail True
    def get_var(self, buffer, name):
        return self.send_sync(ReqMsg('buffer_get_var', *[buffer, name]))

    # Function: buffer_set_var
    # Parameters Buffer: buffer, String: name, Object: value
    # Returns Object
    # Recieves channel id False
    # Can fail True
    def set_var(self, buffer, name, value):
        return self.send_sync(ReqMsg('buffer_set_var', *[buffer, name, value]))

    # Function: buffer_get_option
    # Parameters Buffer: buffer, String: name
    # Returns Object
    # Recieves channel id False
    # Can fail True
    def get_option(self, buffer, name):
        return self.send_sync(ReqMsg('buffer_get_option', *[buffer, name]))

    # Function: buffer_set_option
    # Parameters Buffer: buffer, String: name, Object: value
    # Returns void
    # Recieves channel id False
    # Can fail True
    def set_option(self, buffer, name, value):
        return self.send_sync(ReqMsg('buffer_set_option', *[buffer, name, value]))

    # Function: buffer_get_number
    # Parameters Buffer: buffer
    # Returns Integer
    # Recieves channel id False
    # Can fail True
    def get_number(self, buffer):
        return self.send_sync(ReqMsg('buffer_get_number', *[buffer]))

    # Function: buffer_get_name
    # Parameters Buffer: buffer
    # Returns String
    # Recieves channel id False
    # Can fail True
    def get_name(self, buffer):
        return self.send_sync(ReqMsg('buffer_get_name', *[buffer]))

    # Function: buffer_set_name
    # Parameters Buffer: buffer, String: name
    # Returns void
    # Recieves channel id False
    # Can fail True
    def set_name(self, buffer, name):
        return self.send_sync(ReqMsg('buffer_set_name', *[buffer, name]))

    # Function: buffer_is_valid
    # Parameters Buffer: buffer
    # Returns Boolean
    # Recieves channel id False
    # Can fail False
    def is_valid(self, buffer):
        return self.send_sync(ReqMsg('buffer_is_valid', *[buffer]))

    # Function: buffer_insert
    # Parameters Buffer: buffer, Integer: lnum, ArrayOf(String): lines
    # Returns void
    # Recieves channel id False
    # Can fail True
    def insert(self, buffer, lnum, lines):
        return self.send_sync(ReqMsg('buffer_insert', *[buffer, lnum, lines]))

    # Function: buffer_get_mark
    # Parameters Buffer: buffer, String: name
    # Returns ArrayOf(Integer, 2)
    # Recieves channel id False
    # Can fail True
    def get_mark(self, buffer, name):
        return self.send_sync(ReqMsg('buffer_get_mark', *[buffer, name]))


class Tabpage(Cmd):

    def __init__(self, session):
        self._session = session

    # Function: tabpage_get_windows
    # Parameters Tabpage: tabpage
    # Returns ArrayOf(Window)
    # Recieves channel id False
    # Can fail True
    def get_windows(self, tabpage):
        return self.send_sync(ReqMsg('tabpage_get_windows', *[tabpage]))

    # Function: tabpage_get_var
    # Parameters Tabpage: tabpage, String: name
    # Returns Object
    # Recieves channel id False
    # Can fail True
    def get_var(self, tabpage, name):
        return self.send_sync(ReqMsg('tabpage_get_var', *[tabpage, name]))

    # Function: tabpage_set_var
    # Parameters Tabpage: tabpage, String: name, Object: value
    # Returns Object
    # Recieves channel id False
    # Can fail True
    def set_var(self, tabpage, name, value):
        return self.send_sync(ReqMsg('tabpage_set_var', *[tabpage, name, value]))

    # Function: tabpage_get_window
    # Parameters Tabpage: tabpage
    # Returns Window
    # Recieves channel id False
    # Can fail True
    def get_window(self, tabpage):
        return self.send_sync(ReqMsg('tabpage_get_window', *[tabpage]))

    # Function: tabpage_is_valid
    # Parameters Tabpage: tabpage
    # Returns Boolean
    # Recieves channel id False
    # Can fail False
    def is_valid(self, tabpage):
        return self.send_sync(ReqMsg('tabpage_is_valid', *[tabpage]))


class Vim(Cmd):

    def __init__(self, session):
        self._session = session

    # Function: vim_push_keys
    # Parameters String: str
    # Returns void
    # Recieves channel id False
    # Can fail False
    def push_keys(self, v_str):
        return self.send_sync(ReqMsg('vim_push_keys', *[v_str]))

    # Function: vim_command
    # Parameters String: str
    # Returns void
    # Recieves channel id False
    # Can fail True
    def command(self, v_str):
        return self.send_sync(ReqMsg('vim_command', *[v_str]))

    # Function: vim_feedkeys
    # Parameters String: keys, String: mode
    # Returns void
    # Recieves channel id False
    # Can fail False
    def feedkeys(self, keys, mode):
        return self.send_sync(ReqMsg('vim_feedkeys', *[keys, mode]))

    # Function: vim_replace_termcodes
    # Parameters String: str, Boolean: from_part, Boolean: do_lt, Boolean: special
    # Returns String
    # Recieves channel id False
    # Can fail False
    def replace_termcodes(self, v_str, from_part, do_lt, special):
        return self.send_sync(ReqMsg('vim_replace_termcodes', *[v_str, from_part, do_lt, special]))

    # Function: vim_eval
    # Parameters String: str
    # Returns Object
    # Recieves channel id False
    # Can fail True
    def eval(self, v_str):
        return self.send_sync(ReqMsg('vim_eval', *[v_str]))

    # Function: vim_strwidth
    # Parameters String: str
    # Returns Integer
    # Recieves channel id False
    # Can fail True
    def strwidth(self, v_str):
        return self.send_sync(ReqMsg('vim_strwidth', *[v_str]))

    # Function: vim_list_runtime_paths
    # Parameters 
    # Returns ArrayOf(String)
    # Recieves channel id False
    # Can fail False
    def list_runtime_paths(self, ):
        return self.send_sync(ReqMsg('vim_list_runtime_paths', *[]))

    # Function: vim_change_directory
    # Parameters String: dir
    # Returns void
    # Recieves channel id False
    # Can fail True
    def change_directory(self, v_dir):
        return self.send_sync(ReqMsg('vim_change_directory', *[v_dir]))

    # Function: vim_get_current_line
    # Parameters 
    # Returns String
    # Recieves channel id False
    # Can fail True
    def get_current_line(self, ):
        return self.send_sync(ReqMsg('vim_get_current_line', *[]))

    # Function: vim_set_current_line
    # Parameters String: line
    # Returns void
    # Recieves channel id False
    # Can fail True
    def set_current_line(self, line):
        return self.send_sync(ReqMsg('vim_set_current_line', *[line]))

    # Function: vim_del_current_line
    # Parameters 
    # Returns void
    # Recieves channel id False
    # Can fail True
    def del_current_line(self, ):
        return self.send_sync(ReqMsg('vim_del_current_line', *[]))

    # Function: vim_get_var
    # Parameters String: name
    # Returns Object
    # Recieves channel id False
    # Can fail True
    def get_var(self, name):
        return self.send_sync(ReqMsg('vim_get_var', *[name]))

    # Function: vim_set_var
    # Parameters String: name, Object: value
    # Returns Object
    # Recieves channel id False
    # Can fail True
    def set_var(self, name, value):
        return self.send_sync(ReqMsg('vim_set_var', *[name, value]))

    # Function: vim_get_vvar
    # Parameters String: name
    # Returns Object
    # Recieves channel id False
    # Can fail True
    def get_vvar(self, name):
        return self.send_sync(ReqMsg('vim_get_vvar', *[name]))

    # Function: vim_get_option
    # Parameters String: name
    # Returns Object
    # Recieves channel id False
    # Can fail True
    def get_option(self, name):
        return self.send_sync(ReqMsg('vim_get_option', *[name]))

    # Function: vim_set_option
    # Parameters String: name, Object: value
    # Returns void
    # Recieves channel id False
    # Can fail True
    def set_option(self, name, value):
        return self.send_sync(ReqMsg('vim_set_option', *[name, value]))

    # Function: vim_out_write
    # Parameters String: str
    # Returns void
    # Recieves channel id False
    # Can fail False
    def out_write(self, v_str):
        return self.send_sync(ReqMsg('vim_out_write', *[v_str]))

    # Function: vim_err_write
    # Parameters String: str
    # Returns void
    # Recieves channel id False
    # Can fail False
    def err_write(self, v_str):
        return self.send_sync(ReqMsg('vim_err_write', *[v_str]))

    # Function: vim_report_error
    # Parameters String: str
    # Returns void
    # Recieves channel id False
    # Can fail False
    def report_error(self, v_str):
        return self.send_sync(ReqMsg('vim_report_error', *[v_str]))

    # Function: vim_get_buffers
    # Parameters 
    # Returns ArrayOf(Buffer)
    # Recieves channel id False
    # Can fail False
    def get_buffers(self, ):
        return self.send_sync(ReqMsg('vim_get_buffers', *[]))

    # Function: vim_get_current_buffer
    # Parameters 
    # Returns Buffer
    # Recieves channel id False
    # Can fail False
    def get_current_buffer(self, ):
        return self.send_sync(ReqMsg('vim_get_current_buffer', *[]))

    # Function: vim_set_current_buffer
    # Parameters Buffer: buffer
    # Returns void
    # Recieves channel id False
    # Can fail True
    def set_current_buffer(self, buffer):
        return self.send_sync(ReqMsg('vim_set_current_buffer', *[buffer]))

    # Function: vim_get_windows
    # Parameters 
    # Returns ArrayOf(Window)
    # Recieves channel id False
    # Can fail False
    def get_windows(self, ):
        return self.send_sync(ReqMsg('vim_get_windows', *[]))

    # Function: vim_get_current_window
    # Parameters 
    # Returns Window
    # Recieves channel id False
    # Can fail False
    def get_current_window(self, ):
        return self.send_sync(ReqMsg('vim_get_current_window', *[]))

    # Function: vim_set_current_window
    # Parameters Window: window
    # Returns void
    # Recieves channel id False
    # Can fail True
    def set_current_window(self, window):
        return self.send_sync(ReqMsg('vim_set_current_window', *[window]))

    # Function: vim_get_tabpages
    # Parameters 
    # Returns ArrayOf(Tabpage)
    # Recieves channel id False
    # Can fail False
    def get_tabpages(self, ):
        return self.send_sync(ReqMsg('vim_get_tabpages', *[]))

    # Function: vim_get_current_tabpage
    # Parameters 
    # Returns Tabpage
    # Recieves channel id False
    # Can fail False
    def get_current_tabpage(self, ):
        return self.send_sync(ReqMsg('vim_get_current_tabpage', *[]))

    # Function: vim_set_current_tabpage
    # Parameters Tabpage: tabpage
    # Returns void
    # Recieves channel id False
    # Can fail True
    def set_current_tabpage(self, tabpage):
        return self.send_sync(ReqMsg('vim_set_current_tabpage', *[tabpage]))

    # Function: vim_subscribe
    # Parameters String: event
    # Returns void
    # Recieves channel id True
    # Can fail False
    def subscribe(self, event):
        return self.send_sync(ReqMsg('vim_subscribe', *[event]))

    # Function: vim_unsubscribe
    # Parameters String: event
    # Returns void
    # Recieves channel id True
    # Can fail False
    def unsubscribe(self, event):
        return self.send_sync(ReqMsg('vim_unsubscribe', *[event]))

    # Function: vim_register_provider
    # Parameters String: feature
    # Returns void
    # Recieves channel id True
    # Can fail True
    def register_provider(self, feature):
        return self.send_sync(ReqMsg('vim_register_provider', *[feature]))

    # Function: vim_get_api_info
    # Parameters 
    # Returns Array
    # Recieves channel id True
    # Can fail False
    def get_api_info(self, ):
        return self.send_sync(ReqMsg('vim_get_api_info', *[]))

function_classes = {
    'window': Window,
    'buffer': Buffer,
    'tabpage': Tabpage,
    'vim': Vim,
}

