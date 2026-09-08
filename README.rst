trame-mui: MUI (React) widgets for trame
=============================================

trame-mui is the React equivalent of `trame-vuetify
<https://github.com/Kitware/trame-vuetify>`_: it wraps `MUI
<https://mui.com/>`_ (Material Design components for React, the direct analog
of Vuetify for Vue) for `trame <https://kitware.github.io/trame/>`_
applications running with ``client_type="react"`` (the native React client
that ships with trame-client).

.. code-block:: python

    from trame.app import get_server
    from trame.widgets import mui

    server = get_server(client_type="react")

Not to be confused with `trame-react
<https://github.com/Kitware/trame-react>`_, which embeds a Vue-rendered trame
application inside a React application through an iframe.

.. image:: https://raw.githubusercontent.com/Kitware/trame-mui/refs/heads/master/trame-mui.png
  :alt: Illustration of what can be done with trame and mui


Layout (mirrors trame-vuetify)
------------------------------

* ``react-components/`` - React components + ``install(registry)`` plugin,
  bundled with React as an external, and the Python class generator
* ``src/trame_mui/module/`` - module descriptor (``serve``/``scripts``/
  ``styles``/``react_use``) consumed by ``server.enable_module()``
* ``src/trame_mui/widgets/`` - generated Python widget classes

Development
------------------------------

Build and install the Vue components

.. code-block:: sh

    cd react-components
    npm i
    npm run build
    cd -

Install the library

.. code-block:: sh

    # Create venv and install all dependencies
    uv sync --all-extras --dev

    # Activate environment
    source .venv/bin/activate

    # Install commit analysis
    pre-commit install
    pre-commit install --hook-type commit-msg


License
-------

trame-mui is made available under the MIT License.
