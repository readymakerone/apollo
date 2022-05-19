# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 02:06:44 2022

@author: curti
"""

import math
from lxml import etree
from guitar import Guitar
import pandas as pd

class Apollo(Guitar):
    
    def __init__(self, **kwargs):
        kwargs['svg_name'] = 'apollo.svg'
        kwargs['nut_depth'] = 3.175#mm
        kwargs['binding_thickness'] = 1.5#mm
        Guitar.__init__(self, **kwargs)
        self.led_length = 6#mm
        self.led_width = 5#mm
        self.led_distance = self.scale*(0.5**((self.n_fret-1)/12)-0.5**(self.n_fret/12))/2
        self.led_distances = [0.5] + [self.distance_from_nut(i+1)-self.led_distance for i in range(self.n_fret)]
        self.led_ys = [self.string_positions_at(distance) for distance in self.led_distances]
        
    def export_led_centers(self):
        led_dict = {'y':self.led_distances,
                    **{'string{}'.format(string+1):[self.led_ys[fret][string] for fret in range(self.n_fret+1)] for string in range(self.n_string)}}
        pd.DataFrame(led_dict).to_csv('led_centers.csv')
        
    def pcb_outline(self):
        y_start = self.led_distances[0] - self.led_length/2
        y_end = self.led_distances[-1] - self.led_length/2
        start_width = self.string_spread_at(self.led_distances[0]) + self.led_width
        end_width = self.string_spread_at(self.led_distances[-1]) + self.led_width
        
        pcb_y_start = y_start - self.led_length/2
        pcb_y_end = float(int(self.distance_from_nut(self.n_fret) - self.led_distance + self.led_length/2 + 2 * 2.54 + 1)+1)
        pcb_start_width = start_width + (end_width-start_width)*(pcb_y_start - y_start)/(y_end-y_start) + 0.5
        pcb_end_width = start_width + (end_width - start_width)*(pcb_y_end - y_start)/(y_end-y_start) + 0.5
        
        return [(pcb_y_start,-pcb_start_width/2),
                (pcb_y_end, -pcb_end_width/2),
                (pcb_y_end, pcb_end_width/2),
                (pcb_y_start, pcb_start_width/2)]
        
    
    def draw_leds(self):
        NSMAP = self.__class__.NSMAP
        CIRCLE_STYLE = "fill:none;stroke-width:0;stroke-miterlimit:4;stroke-dasharray:none"
        LINE_STYLE = "fill:none;stroke:#000000;stroke-width:0;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
        lc_layer = etree.SubElement(self.root,
                                     'g',
                                     **{'{%s}groupmode'%NSMAP['inkscape']:'layer',
                                        'id':'ledcenters',
                                        '{%s}label'%NSMAP['inkscape']:'LED Centers',
                                        'style': 'display:inline'})
        lo_layer = etree.SubElement(self.root,
                                     'g',
                                     **{'{%s}groupmode'%NSMAP['inkscape']:'layer',
                                        'id':'ledoutlines',
                                        '{%s}label'%NSMAP['inkscape']:'LED Outlines',
                                        'style': 'display:inline'})
        
        pcboutline = etree.SubElement(lo_layer,
                                      'path',
                                      **{'style':LINE_STYLE,
                                         'd':self.path_string([(self.x0-x, self.y0+y) for (x,y) in self.pcb_outline()], True),
                                         'id':'pcboutline'})
         
        for fret in range(self.n_fret+1):
            for string in range(self.n_string):
                led_cx = self.x0 - self.led_distances[fret]
                led_cy = self.y0 + self.led_ys[fret][string]
                circle = etree.SubElement(lc_layer,
                                          'circle',
                                          **{'style':CIRCLE_STYLE,
                                             'id':'led{}-{}'.format(fret, string),
                                             'cx':str(led_cx),
                                             'cy':str(led_cy),
                                             'r':str(1.5875)})
                rect = etree.SubElement(lo_layer,
                                       'rect',
                                       style='fill:none;fill-rule:evenodd;stroke-width:0;stroke:#000000;stroke-opacity:1',
                                       id='led-outline{}-{}'.format(fret, string),
                                       width=str(self.led_length),
                                       height=str(self.led_width),
                                       x=str(led_cx - self.led_length/2),
                                       y=str(led_cy - self.led_width/2))
        

a = Apollo()
a.draw()
a.draw_leds()
a.save_svg()
a.export_led_centers()