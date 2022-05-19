# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 22:16:03 2022

@author: curti
"""

# importing pycairo
import cairo
from lxml import etree
import math
  
class Guitar():
    
    NSMAP = {None:"http://www.w3.org/2000/svg",
             'dc':"http://purl.org/dc/elements/1.1/",
             'cc':"http://creativecommons.org/ns#",
             'rdf':"http://www.w3.org/1999/02/22-rdf-syntax-ns#",
             'svg':"http://www.w3.org/2000/svg",
             'xlink':"http://www.w3.org/1999/xlink",
             'sodipodi':"http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
             'inkscape':"http://www.inkscape.org/namespaces/inkscape"}
    
    GIBSON_STYLE = {'scale':623.9,#mm, 24.562 inches, per StewMac specs
                    'nut_width':44.5#mm, per StewMac specs
                    'nut_string_spread':35.56#mm, per StewMac specs
                    'bridge_string_spread':52#mm,
                    'n_fret':22,
                    'tuners':(3,3),
                    'nut_depth':4.8}
    
    FENDER_STYLE = {'scale':623.9,#mm, 24.562 inches, per StewMac specs
                    'nut_width':44.5#mm, per StewMac specs
                    'nut_string_spread':35.56#mm, per StewMac specs
                    'bridge_string_spread':52#mm,
                    'n_fret':22,
                    'tuners':(3,3),
                    'nut_depth':4.8}
    
    def __init__(self, **kwargs):
        self.scale = kwargs['scale'] if 'scale' in kwargs else 623.9#mm
        self.nut_width = kwargs['nut_width'] if 'nut_width' in kwargs else 44.5#mm
        self.nut_string_spread = kwargs['nut_string_spread'] if 'nut_string_spread' in kwargs else 35.56#mm
        self.bridge_string_spread = kwargs['bridge_string_spread'] if 'bridge_string_spread' in kwargs else 52#mm
        self.n_fret = kwargs['n_fret'] if 'n_fret' in kwargs else 22
        self.tuners = kwargs['tuners'] if 'tuners' in kwargs else (6, 0)
        self.n_string = self.tuners[0] + self.tuners[1]
        self.delta = (self.nut_width - self.nut_string_spread)/2
        self.nut_depth = kwargs['nut_depth'] if 'nut_depth' in kwargs else 4.8#mm
        if self.tuners[0]*self.tuners[1] == 0:
            self.tuner_incline = 18#degrees
            first_tuner = 40
            
        else:
            self.tuner_incline = 12#degrees
            first_tuner = 50
        self.tuner_post_r = 3#mm
        self.tuner_hole_r = 4.165#mm
        tuner_x_delta = self.nut_string_spread/(5*math.tan(math.radians(self.tuner_incline)))
        self.l_tuners = [first_tuner+i*tuner_x_delta for i in range(tuners[0])]
        self.r_tuners = [first_tuner+i*tuner_x_delta for i in range(tuners[1])]
        
    def distance_from_nut(self, fret):
        return self.scale*(1-0.5**(fret/12))
    
    def string_spread_at(self, distance_from_nut):
        return self.nut_string_spread + (self.bridge_string_spread - self.nut_string_spread)*distance_from_nut/self.scale
    
    def fretboard_width_at(self, distance_from_nut):
        return self.string_spread_at(distance_from_nut) + 2*self.delta
    
    def string_positions_at(self, distance_from_nut):
        spread = self.string_spread_at(distance_from_nut)
        return [spread*(i/5-1/2) for i in range(self.n_string)]
    
    def path_string(self, coords, close=False):
        coords = [(0,0)]+coords
        string = ' '.join([str(coords[i+1][0]-coords[i][0])+','+str(coords[i+1][1]-coords[i][1]) for i in range(len(coords[1:]))])
        if close:
            string += ' z'
        return 'm ' + string
    
    def draw(self, docwidth=1300, docheight=450, docunit='mm'):
        x0, y0 = 1000, docheight/2
        NSMAP = self.__class__.NSMAP
        SVG_ATTRIB = {'width':"{}mm".format(docwidth),
                      'height':"{}mm".format(docheight),
                      'viewBox':"0 0 1300 450",
                      'version':"1.1",
                      'id':"svg1831"}
        LINE_STYLE = "fill:none;stroke:#000000;stroke-width:0;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
        CIRCLE_STYLE = "fill:none;stroke-width:0;stroke-miterlimit:4;stroke-dasharray:none"
        
        root = etree.Element('svg', nsmap = NSMAP, **SVG_ATTRIB)
        defs = etree.SubElement(root, 'defs')
        defs.attrib['id']='defs1825'
        namedview = etree.SubElement(root, 
                                     '{%s}namedview'%(NSMAP['sodipodi']),
                                     **{'id':'base',
                                        'pagecolor':'#ffffff',
                                        'bordercolor':'#666666',
                                        'borderopacity':'1.0',
                                        '{%s}pageopacity'%NSMAP['inkscape']:'0.0',
                                        '{%s}pageshadow'%NSMAP['inkscape']:'2',
                                        '{%s}zoom'%NSMAP['inkscape']:'1',
                                        '{%s}cx'%NSMAP['inkscape']:'3465.875',
                                        '{%s}cy'%NSMAP['inkscape']:'769',
                                        '{%s}document-units'%NSMAP['inkscape']:docunit,
                                        '{%s}current-layer'%NSMAP['inkscape']: 'layer1',
                                        'showgrid':'false',
                                        'showguide':'false',
                                        '{%s}guide-bbox'%NSMAP['inkscape']:'true',
                                        '{%s}window-width'%NSMAP['inkscape']:'1920',
                                        '{%s}window-height'%NSMAP['inkscape']:'1017',
                                        '{%s}window-x'%NSMAP['inkscape']:'-8',
                                        '{%s}window-y'%NSMAP['inkscape']:'-8',
                                        '{%s}window-maximized'%NSMAP['inkscape']:'1',
                                        '{%s}pagecheckerboard'%NSMAP['inkscape']:'0'})

        centerline = etree.SubElement(namedview,
                                     '{%s}guide'%(NSMAP['sodipodi']),
                                     **{'position':str(x0)+','+str(y0),
                                        'orientation':'0,1',
                                        'id':'guide0001',
                                        '{%s}locked'%NSMAP['inkscape']:'true'})
        nut_guide = etree.SubElement(namedview,
                                     '{%s}guide'%(NSMAP['sodipodi']),
                                     **{'position':str(x0)+','+str(y0),
                                        'orientation':'1,0',
                                        'id':'guide0002',
                                        '{%s}locked'%NSMAP['inkscape']:'true'})
        bridge_guide = etree.SubElement(namedview,
                                        '{%s}guide'%(NSMAP['sodipodi']),
                                        **{'position':str(x0-self.scale)+','+str(y0),
                                           'orientation':'1,0',
                                           'id':'guide0003',
                                           '{%s}locked'%NSMAP['inkscape']:'true'})
        
        harmonic_guide = etree.SubElement(namedview,
                                          '{%s}guide'%(NSMAP['sodipodi']),
                                          **{'position':str(x0-self.distance_from_nut(24))+','+str(y0),
                                             'orientation':'1,0',
                                             'id':'guide0004',
                                             '{%s}locked'%(NSMAP['inkscape']):'true'})

        md = etree.SubElement(root, 'metadata', id='metadata1828')
        rdf = etree.SubElement(md, '{%s}RDF'%NSMAP['rdf'])
        work = etree.SubElement(rdf, '{%s}Work'%NSMAP['cc'])
        work.attrib['{%s}about'%NSMAP['rdf']] = ''
        f = etree.SubElement(work, '{%s}format'%NSMAP['dc'])
        f.text = 'image/svg+xml'
        t = etree.SubElement(work, '{%s}type'%NSMAP['dc'])
        t.attrib['{%s}resource'%NSMAP['rdf']] = 'http://purl.org/dc/dcmitype/StillImage'
        
        #draw fretboard
        fretboard_length = self.distance_from_nut(self.n_fret + 0.85)
        fretboard_end_half_width = self.fretboard_width_at(fretboard_length)/2
        fretboard_start_half_width = self.nut_width/2
        board_path_coords =[(x0-fretboard_length, y0+fretboard_end_half_width),
                            (x0-fretboard_length, y0-fretboard_end_half_width),
                            (x0, y0-fretboard_start_half_width),
                            (x0, y0+fretboard_start_half_width)]
        g = etree.SubElement(root,
                             'g',
                             **{'{%s}groupmode'%NSMAP['inkscape']:'layer',
                                'id':'fretboard',
                                '{%s}label'%NSMAP['inkscape']:'Fretboard',
                                'style': 'display:inline'})
        board_path = etree.SubElement(g,
                                      'path',
                                      **{'style':LINE_STYLE,
                                         'd':self.path_string(board_path_coords, True),
                                         'id':'path0001'})
        for i in range(self.n_fret):
            fret = i+1
            x_dis = self.distance_from_nut(fret)
            y_dis = self.fretboard_width_at(x_dis)/2
            fret_coords = [(x0-x_dis, y0+y_dis),
                           (x0-x_dis, y0-y_dis)]
            fret_path = etree.SubElement(g,
                                         'path',
                                         **{'style':LINE_STYLE,
                                            'd':self.path_string(fret_coords),
                                            'id':'path{}'.format(str(fret+100).zfill(4))})
        
        nut_string_y = self.string_positions_at(0)
        bridge_string_y = self.string_positions_at(self.scale)
        for i in range(self.n_string):
            string_coords = [(x0, y0+nut_string_y[i]),
                             (x0-self.scale, y0+bridge_string_y[i])]
            string_path = etree.SubElement(g,
                                           'path',
                                           **{'style':LINE_STYLE,
                                              'd':self.path_string(string_coords),
                                              'id':'path{}'.format(str(i+201).zfill(4))})
        
        
        for tuner in range(len(self.l_tuners)):
            tuner_x = x0 + self.l_tuners[tuner]
            string_y = y0 + self.string_positions_at(0)[tuner]
            tuner_y = string_y - self.tuner_post_r
            
            if tuner == 0:
                headstock_start_x = tuner_x+13*math.sin(math.radians(self.tuner_incline))-self.tuner_hole_r*math.cos(math.radians(self.tuner_incline))
                headstock_start_y = tuner_y-13*math.cos(math.radians(self.tuner_incline))-self.tuner_hole_r*math.sin(math.radians(self.tuner_incline))
            if tuner == len(self.l_tuners)-1:
                headstock_end_x = tuner_x+13*math.sin(math.radians(self.tuner_incline))+self.tuner_hole_r*math.cos(math.radians(self.tuner_incline))
                headstock_end_y = tuner_y-13*math.cos(math.radians(self.tuner_incline))+self.tuner_hole_r*math.sin(math.radians(self.tuner_incline))
                headstock_path = etree.SubElement(g,
                                                  'path',
                                                  **{'style':LINE_STYLE,
                                                     'd':self.path_string([(headstock_start_x, headstock_start_y), (headstock_end_x, headstock_end_y)]),
                                                     'id':'path{}'.format(str(500).zfill(4))})
                
            circle = etree.SubElement(g,
                                      'circle',
                                      **{'style':CIRCLE_STYLE,
                                         'id':'path{}'.format(str(tuner+301).zfill(4)),
                                         'cx':str(tuner_x),
                                         'cy':str(tuner_y),
                                         'r':str(self.tuner_post_r)})
            circle = etree.SubElement(g,
                                      'circle',
                                      **{'style':CIRCLE_STYLE,
                                         'id':'path{}'.format(str(tuner+401).zfill(4)),
                                         'cx':str(tuner_x),
                                         'cy':str(tuner_y),
                                         'r':str(self.tuner_hole_r)})
            fret_path = etree.SubElement(g,
                                         'path',
                                         **{'style':LINE_STYLE,
                                            'd':self.path_string([(x0, string_y), (tuner_x, string_y)]),
                                            'id':'path{}'.format(str(tuner+502).zfill(4))})
        
        for tuner in range(len(self.r_tuners)):
            tuner_index = len(self.l_tuners) + tuner
            tuner_x = x0 + self.r_tuners[-(1+tuner)]
            string_y = y0 + self.string_positions_at(0)[tuner_index]
            tuner_y = string_y +  self.tuner_post_r
            
            if tuner == 0:
                headstock_end_x = tuner_x+13*math.sin(math.radians(self.tuner_incline))+self.tuner_hole_r*math.cos(math.radians(self.tuner_incline))
                headstock_end_y = tuner_y+13*math.cos(math.radians(self.tuner_incline))-self.tuner_hole_r*math.sin(math.radians(self.tuner_incline))
            if tuner == len(self.r_tuners)-1:
                headstock_start_x = tuner_x+13*math.sin(math.radians(self.tuner_incline))-self.tuner_hole_r*math.cos(math.radians(self.tuner_incline))
                headstock_start_y = tuner_y+13*math.cos(math.radians(self.tuner_incline))+self.tuner_hole_r*math.sin(math.radians(self.tuner_incline))
                headstock_path = etree.SubElement(g,
                                                  'path',
                                                  **{'style':LINE_STYLE,
                                                     'd':self.path_string([(headstock_start_x, headstock_start_y), (headstock_end_x, headstock_end_y)]),
                                                     'id':'path{}'.format(str(501).zfill(4))})
                
            circle = etree.SubElement(g,
                                      'circle',
                                      **{'style':CIRCLE_STYLE,
                                         'id':'path{}'.format(str(tuner_index+301).zfill(4)),
                                         'cx':str(tuner_x),
                                         'cy':str(tuner_y),
                                         'r':str(self.tuner_post_r)})
            circle = etree.SubElement(g,
                                      'circle',
                                      **{'style':CIRCLE_STYLE,
                                         'id':'path{}'.format(str(tuner_index+401).zfill(4)),
                                         'cx':str(tuner_x),
                                         'cy':str(tuner_y),
                                         'r':str(self.tuner_hole_r)})
            fret_path = etree.SubElement(g,
                                         'path',
                                         **{'style':LINE_STYLE,
                                            'd':self.path_string([(x0, string_y), (tuner_x, string_y)]),
                                            'id':'path{}'.format(str(tuner_index+502).zfill(4))})
        
        for i in range(self.n_fret):
            fret = i+1
            dot_x = x0 - (self.distance_from_nut(fret) + self.distance_from_nut(i))/2
            dot_r = 2.375
            if fret%12 in [3,5,7,9]:
                dot_ys = [y0]
            elif fret%12 == 0:
                f_width = self.fretboard_width_at(dot_x)
                dot_ys = [y0 + i*1.5*f_width/7 for i in [-1, 1]]
            else:
                dot_ys = []
                
            for dot_y in dot_ys:
                dot = etree.SubElement(g,
                                       'circle',
                                       **{'style':CIRCLE_STYLE,
                                          'id':'path{}'.format(str(fret+600).zfill(4)),
                                          'cx':str(dot_x),
                                          'cy':str(dot_y),
                                          'r':str(dot_r)})
            
            
        nut = etree.SubElement(g,
                                'rect',
                                style='fill:none;fill-rule:evenodd;stroke-width:0;stroke:#000000;stroke-opacity:1',
                                id='rect0701',
                                width=str(self.nut_depth),
                                height=str(self.nut_width),
                                x=str(x0),
                                y=str(y0-self.nut_width/2))
        
        mounting_hole_sep = 77.5#mm
        humbucker_height = 70#mm
        humbucker_width = 38#mm
        wing_height = 7#mm
        wing_width = 13#mm
        hum_ring_height = 89#mm
        hum_ring_width = 45#mm
        c_hum_coords = [(humbucker_width/2, humbucker_height/2),
                        (wing_width/2, humbucker_height/2),
                        (wing_width/2, wing_height + humbucker_height/2),
                        (-wing_width/2, wing_height + humbucker_height/2),
                        (-wing_width/2, humbucker_height/2),
                        (-humbucker_width/2, humbucker_height/2),
                        (-humbucker_width/2, -humbucker_height/2),
                        (-wing_width/2, -humbucker_height/2),
                        (-wing_width/2, -wing_height-humbucker_height/2),
                        (wing_width/2, -wing_height-humbucker_height/2),
                        (wing_width/2, -humbucker_height/2),
                        (humbucker_width/2, -humbucker_height/2)]
        c_ring_coords = [(hum_ring_width/2, hum_ring_height/2),
                         (-hum_ring_width/2, hum_ring_height/2),
                         (-hum_ring_width/2, -hum_ring_height/2),
                         (hum_ring_width/2, -hum_ring_height/2)]
        r_hum_coords = [(x-humbucker_width/4, y) for (x,y) in c_hum_coords]
        r_ring_coords = [(x-humbucker_width/4, y) for (x,y) in c_ring_coords]
        l_hum_coords = [(x+humbucker_width/4, y) for (x,y) in c_hum_coords]
        l_ring_coords = [(x+humbucker_width/4, y) for (x,y) in c_ring_coords]
        neck_pole_position = min(x0-self.distance_from_nut(24), x0-fretboard_length-hum_ring_width/2 + humbucker_width/4 - 1)
        neck_pickup = etree.SubElement(g,
                                       'path',
                                       **{'style':LINE_STYLE,
                                          'd':self.path_string([(neck_pole_position+x, y0+y) for (x,y) in r_hum_coords], True),
                                          'id':'path0901'})
        neck_ring = etree.SubElement(g,
                                       'path',
                                       **{'style':LINE_STYLE,
                                          'd':self.path_string([(neck_pole_position+x, y0+y) for (x,y) in r_ring_coords], True),
                                          'id':'path0902'})
        neck_mount_hole_bot = etree.SubElement(g,
                                               'circle',
                                               **{'style':CIRCLE_STYLE,
                                                  'id':'path0903',
                                                  'cx':str(neck_pole_position-humbucker_width/4),
                                                  'cy':str(y0-mounting_hole_sep/2),
                                                  'r':'0.75'})
        neck_mount_hole_top = etree.SubElement(g,
                                               'circle',
                                               **{'style':CIRCLE_STYLE,
                                                  'id':'path0904',
                                                  'cx':str(neck_pole_position-humbucker_width/4),
                                                  'cy':str(y0+mounting_hole_sep/2),
                                                  'r':'0.75'})
        
        bridge_start_position = x0-self.scale+0.75*25.4
        bridge_pickup = etree.SubElement(g,
                                       'path',
                                       **{'style':LINE_STYLE,
                                          'd':self.path_string([(bridge_start_position+hum_ring_width/2+x, y0+y) for (x,y) in c_hum_coords], True),
                                          'id':'path0905'})
        bridge_ring = etree.SubElement(g,
                                       'path',
                                       **{'style':LINE_STYLE,
                                          'd':self.path_string([(bridge_start_position+hum_ring_width/2+x, y0+y) for (x,y) in c_ring_coords], True),
                                          'id':'path0906'})
        bridge_mount_hole_bot = etree.SubElement(g,
                                                'circle',
                                                **{'style':CIRCLE_STYLE,
                                                   'id':'path0907',
                                                   'cx':str(bridge_start_position+hum_ring_width/2),
                                                   'cy':str(y0-mounting_hole_sep/2),
                                                   'r':'0.75'})
        bridge_mount_hole_top = etree.SubElement(g,
                                                'circle',
                                                **{'style':CIRCLE_STYLE,
                                                   'id':'path0908',
                                                   'cx':str(bridge_start_position+hum_ring_width/2),
                                                   'cy':str(y0+mounting_hole_sep/2),
                                                   'r':'0.75'})
        
        with open("./output.svg", "wb") as f:
            f.write(etree.tostring(root,
                                   pretty_print = True,
                                   xml_declaration=True,
                                   encoding="UTF-8",
                                   standalone=False))


  
  
f = Fretboard(tuners=(3,3))
f.draw()