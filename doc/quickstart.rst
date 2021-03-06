.. _quickstart:

==========
Quickstart
==========

Installation
------------

Assure you have at least tmux **>= 1.8** and python **>= 2.6**. For Ubuntu 12.04/12.10/13.04 users, you can download the tmux 1.8 package for Ubuntu 13.10 from `https://launchpad.net/ubuntu/+source/tmux <https://launchpad.net/ubuntu/+source/tmux>`_ and install it using dpkg.

.. code-block:: bash

    $ pip install tmuxp

You can upgrade to the latest release with:

.. code-block:: bash

    $ pip install tmuxp -U

Then install :ref:`bash_completion`.

CLI
---

.. seealso:: :ref:`examples`, :ref:`cli`, :ref:`bash_completion`.

tmuxp launches workspaces / sessions from JSON and YAML files.

Configuration files can be stored in ``$HOME/.tmuxp`` or in project
directories as ``.tmuxp.py``, ``.tmuxp.json`` or ``.tmuxp.yaml``.

Every configuration is required to have:

1. ``session_name``
2. list of ``windows``
3. list of ``panes`` for every window in ``windows``

Create a file, ``~/.tmuxp/example.yaml``:

.. literalinclude:: ../examples/2-pane-vertical.yaml
    :language: yaml

.. code-block:: bash

    $ tmuxp load example.yaml

This creates your tmuxp session.

Load multiple tmux sessions at once:

.. code-block:: bash

    $ tmuxp load example.yaml anothersession.yaml

tmuxp will offer to ``switch-client`` for you if you're already in a
session.

You can also `Import`_ configs `teamocil`_ and `tmuxinator`_.

.. _Import: http://tmuxp.readthedocs.io/en/latest/cli.html#import
.. _tmuxinator: https://github.com/aziz/tmuxinator
.. _teamocil: https://github.com/remiprev/teamocil



Pythonics
---------

.. seealso::
    :ref:`libtmux python API documentation <libtmux:api>` and :ref:`developing`,
    :ref:`internals`.


ORM - `Object Relational Mapper`_

AL - `Abstraction Layer`_

.. _Abstraction Layer: http://en.wikipedia.org/wiki/Abstraction_layer
.. _Object Relational Mapper: http://en.wikipedia.org/wiki/Object-relational_mapping

python abstraction layer
""""""""""""""""""""""""

======================================== =================================
:ref:`tmuxp python api <libtmux:api>`    :term:`tmux(1)` equivalent
======================================== =================================
:meth:`libtmux.Server.new_session`       ``$ tmux new-session``
:meth:`libtmux.Server.list_sessions`     ``$ tmux list-sessions``
:meth:`libtmux.Session.list_windows`     ``$ tmux list-windows``
:meth:`libtmux.Session.new_window`       ``$ tmux new-window``
:meth:`libtmux.Window.list_panes`        ``$ tmux list-panes``
:meth:`libtmux.Window.split_window`      ``$ tmux split-window``
:meth:`libtmux.Pane.send_keys`           ``$ tmux send-keys``
======================================== =================================
