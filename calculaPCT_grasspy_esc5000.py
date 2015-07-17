import grass.script as grass
import os
#mapa de vegetacao
vegetacao="vegetacao_natural_cli_rast_30m_tif"
mapa="mosaic_topodata_30m_extract_tif_5000_30m_vect"
length=1
os.chdir(r'E:\data_2015\___john\Tadeu_finlandia\TXTs_PCT\esc_5000')


def stats_area(mapa,id_map):
    id_map=id_map.replace('\n','')
    acumla_area=0
    grass.run_command('g.region',rast=mapa)
    x=grass.read_command('r.stats',flags='a',input=mapa)
    y=x.split('\n')
    del y[-1];del y[-1]
    
    #for aculuma area_m2 
    for i in y:
        split=i.split(' ')
        area_m2=float(split[1])
        acumla_area=acumla_area+area_m2
    
    txt=open('basin_'+id_map+'.txt','w')
    cabecalho='id'',''pct_veg\n'
    txt.write(cabecalho)    
    
    for i in y:
        split=i.split(' ')    
        id=split[0]
        area_m2=float(split[1])
        pct=round(area_m2/acumla_area*100,3)
        txt.write(id+','+`pct`+'\n')
        
    txt.close()



#stats_area("mapa_soma_int",5965)

def create_bins(mapa_temp):
    vegetacao="vegetacao_natural_cli_rast_30m_tif"
    expressao1='veg_temp=if('+mapa_temp+'>0,'+vegetacao+',null())'
    grass.mapcalc(expressao1, overwrite = True, quiet = True)
    grass.run_command('r.series',inpu='veg_temp,'+mapa_temp,out='mapa_soma',method='sum',overwrite=True)
    expressao2='mapa_soma_int=int(mapa_soma)'
    grass.mapcalc(expressao2, overwrite = True, quiet = True)    
    return 'mapa_soma_int'



def stats(mapa):
    grass.run_command('g.region',vect=mapa)
    con=6039
    while con <= 6268:
        query="id=%d"%con
        
        x=grass.read_command('v.db.select', flags='c', map=mapa, column='id', where=query,verbose=False)
        grass.run_command('v.extract', input=mapa, output='temp', where=query, type='area', new=1,overwrite=True,verbose=False) 
        grass.run_command('v.to.rast', input='temp', out='temp_rast_masc', use="cat",overwrite=True,verbose=False)
        grass.run_command('r.mask',input="temp_rast_masc",overwrite=True)
        
        mapa_soma=create_bins("temp_rast_masc")
        stats_area(mapa_soma,x)
        
        grass.run_command('g.remove',flags='f',rast=mapa_soma+',mapa_soma_int')
        grass.run_command('g.remove',flags='f',vect='temp')
        grass.run_command('r.mask',flags='r')
        grass.run_command('g.remove',flags='f',rast='temp_rast_masc')
        con=con+1
    


stats(mapa)
   
    