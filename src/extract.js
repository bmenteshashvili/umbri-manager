const topo=require('/home/claude/gui/build/node_modules/world-atlas/countries-50m.json');
const tc=require('/home/claude/gui/build/node_modules/topojson-client');
const fc=tc.feature(topo,topo.objects.countries);
const B=[-11,34,48,71];const out=[];
for(const f of fc.features){const g=f.geometry;if(!g)continue;
 const polys=g.type==='Polygon'?[g.coordinates]:g.coordinates;const keep=[];
 for(const p of polys){const r=p[0];if(r.some(([x,y])=>x>B[0]&&x<B[2]&&y>B[1]&&y<B[3])){
   let pts=[];let last=null;for(const [x,y] of r){const q=[+x.toFixed(2),+y.toFixed(2)];if(!last||Math.abs(q[0]-last[0])+Math.abs(q[1]-last[1])>0.04){pts.push(q);last=q}}
   if(pts.length>3)keep.push(pts)}}
 if(keep.length)out.push({n:f.properties.name,p:keep})}
require('fs').writeFileSync('/home/claude/gui/geo.json',JSON.stringify(out));
console.log(out.length, out.map(o=>o.n).join(', '), require('fs').statSync('/home/claude/gui/geo.json').size);
