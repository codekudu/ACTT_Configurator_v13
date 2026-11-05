from pathlib import Path
import json
folder=Path(__file__).parent/'models'; manifest=folder/'manifest.json'; old={}
if manifest.exists():
 try:
  data=json.loads(manifest.read_text())
  for item in data.get('models',data if isinstance(data,list) else []): old[item.get('obj')]=item
 except Exception: pass
items=[]
for obj in sorted(folder.glob('*.obj')):
 e=old.get(obj.name,{})
 e.update({'name':e.get('name',obj.stem.replace('_',' ').title()),'obj':obj.name,'enabled':e.get('enabled',True),'position':e.get('position',[0,0,0]),'rotation':e.get('rotation',[0,0,0]),'scale':e.get('scale',[1,1,1])})
 mtl=obj.with_suffix('.mtl')
 if mtl.exists(): e['mtl']=mtl.name
 else: e.pop('mtl',None)
 items.append(e)
manifest.write_text(json.dumps({'coordinateSystem':'base-model-local','models':items},indent=2)+'\n')
print(f'Indexed {len(items)} model(s). Refresh the browser with Ctrl+F5.')
