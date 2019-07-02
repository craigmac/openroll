#############################################################################
##
# Copyright (C) 2018 The Qt Company Ltd.
# Contact: http://www.qt.io/licensing/
##
# This file is part of the Qt for Python examples of the Qt Toolkit.
##
# $QT_BEGIN_LICENSE:BSD$
# You may use this file under the terms of the BSD license as follows:
##
# "Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in
# the documentation and/or other materials provided with the
# distribution.
# * Neither the name of The Qt Company Ltd nor the names of its
# contributors may be used to endorse or promote products derived
# from this software without specific prior written permission.
##
##
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
# $QT_END_LICENSE$
##
#############################################################################

"""fbs entry point for building executable."""


import sys

from fbs_runtime.application_context.PySide2 import ApplicationContext

from windows import Control_Window


class AppContext(ApplicationContext):
    """From https://doc.qt.io/qtforpython/deployment-fbs.html
    1. Subclass ApplicationContext
    2. implement run()
    3. end run() with self.app.exec_()
    4. Create instance of AppContext
    5. Invoke run() method
    """
    def run(self):
        """fbs tooling required entrypoint."""
        window = Control_Window(self.build_settings['version'])
        version = self.build_settings['version']
        window.setWindowTitle("Openroll {}".format(version))
        window.resize(800, 600)
        window.show()
        return self.app.exec_()


if __name__ == '__main__':
    app_ctx = AppContext()
    sys.exit(app_ctx.run())
