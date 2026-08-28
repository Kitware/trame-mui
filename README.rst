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
    from trame_mui.widgets import mui

    server = get_server(client_type="react")

Not to be confused with `trame-react
<https://github.com/Kitware/trame-react>`_, which embeds a Vue-rendered trame
application inside a React application through an iframe.

Layout (mirrors trame-vuetify)
------------------------------

* ``react-components/`` - React components + ``install(registry)`` plugin,
  bundled with React as an external, and the Python class generator
* ``trame_mui/module/`` - module descriptor (``serve``/``scripts``/
  ``styles``/``react_use``) consumed by ``server.enable_module()``
* ``trame_mui/widgets/`` - generated Python widget classes

License
-------

trame-mui is made available under the MIT License.
