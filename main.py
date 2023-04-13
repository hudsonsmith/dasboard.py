import pynvim


@pynvim.plugin
class TestPlugin(object):
    def __init__(self, nvim) -> None:
        self.nvim = nvim
        self.showed_greeter = False
        self.toggled_lines = False

        self.messages: list = [
            "Welcome to Vim!",
           "    We hope you enjoy your stay."
        ]

    @pynvim.autocmd("VimEnter", eval='expand("<afile>")', sync=True)
    def on_buf_enter(self, filename) -> None:
        if self.showed_greeter == True:
            if self.toggled_lines == False:
                self.nvim.command("set nu")
                self.toggled_lines = True

            return

        self.showed_greeter = True

        argc = self.nvim.eval("v:argv")

        #self.nvim.current.line = (f"Argc: {argc}, Filename: '{len(filename)}'")

        if len(argc) == 2 and len(filename) <= 0:
            self.nvim.command("set nonu")
            buffer: pynvim.Buffer = self.nvim.current.buffer

            for i, line in enumerate(self.messages):
                buffer.append(line)

