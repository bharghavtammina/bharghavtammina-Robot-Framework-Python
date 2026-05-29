# API Method Examples (Robot Framework)

Live demo API used in all files:
- https://restful-booker.herokuapp.com

Shared setup is in `resources/api_booker.resource`.

Files:
- `api_get.robot`
- `api_post.robot`
- `api_put.robot`
- `api_patch.robot`
- `api_delete.robot`

Run one file:

```powershell
robot --outputdir results tests/examples/api/api_get.robot
```

Run all API files:

```powershell
robot --outputdir results tests/examples/api/api_*.robot
```
