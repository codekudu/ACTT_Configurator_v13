ACTT Configurator v11

The command-window lines such as GET /tinker.obj 200 were normal Python web-server request logs, not model errors. The favicon.ico 404 was also harmless.

V11 changes:
- Uses serve.py with request logging suppressed.
- Handles /favicon.ico with HTTP 204 so the 404 disappears.
- start-viewer.bat always rebuilds the optional model manifest before launch.
- refresh-models.bat updates the manifest without trying to start a second HTTP server. Use this while the website is already running, then Ctrl+F5 the browser.
- refresh-models-and-start.bat remains available for a fresh launch.

Recommended workflow:
1. Copy OBJ/MTL/texture files into models/.
2. If viewer is closed: run start-viewer.bat.
3. If viewer is already open: run refresh-models.bat, then Ctrl+F5.
4. Leave the small command window open while using the site because it is the local web server. It will now remain quiet unless there is an actual Python error.
