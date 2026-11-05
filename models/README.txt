OPTIONAL MODEL FOLDER

1. Copy each OBJ and matching MTL into this models folder. Keep texture files here too if the MTL refers to them.
2. Run refresh-models-and-start.bat from the main folder.
3. Refresh the browser with Ctrl+F5 after later additions.

WHY THE AIRLINES MODEL DID NOT APPEAR IN V9
V9 loaded folder models into the scene root, while the ACTT base model is rotated -90 degrees and vertically grounded. The manifest entry existed and the OBJ loaded, but the airlines geometry remained in its original CAD coordinate frame, commonly placing it outside or perpendicular to the visible truck. V10 parents folder models to the ACTT base model, so same-assembly exports inherit the ACTT rotation and ground offset.

If an independently exported model uses a different origin, adjust position, rotation and scale in manifest.json. Rotation values are radians. Example 90 degrees = 1.570796.
