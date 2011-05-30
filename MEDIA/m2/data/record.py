# Recorded script from Mayavi2
from numpy import array
try:
    engine = mayavi.engine
except NameError:
    from enthought.mayavi.api import Engine
    engine = Engine()
    engine.start()
if len(engine.scenes) == 0:
    engine.new_scene()
# ------------------------------------------- 
scene = engine.scenes[0]
vtkxml_file_reader = engine.open(u'/Users/prabhu/work/MEDIA/m2/data/solution.vtp', scene)
from enthought.mayavi.modules.surface import Surface
surface = Surface()
engine.add_filter(surface, vtkxml_file_reader)
scene.scene.camera.position = [-5.0805380472988206, -22.772737120755238, 27.951999647518075]
scene.scene.camera.focal_point = [-0.30313491821289062, 0.0, 1.4027749300003052]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.1142423672711194, 0.76412329986979977, 0.63487342369670707]
scene.scene.camera.clipping_range = [22.838642391722981, 51.077591804257452]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-26.79814746753679, -17.616423028517339, 16.698474306673273]
scene.scene.camera.focal_point = [-0.30313491821289062, 0.0, 1.4027749300003052]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.117668827287714, 0.54423876670086724, 0.83063723243342136]
scene.scene.camera.clipping_range = [16.95271984178639, 58.486755617116714]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
surface.actor.property.edge_visibility = True
surface.actor.property.line_width = 1.0908000469207764
surface.actor.property.line_width = 1.0908
vtkxml_file_reader1 = engine.open(u'/Users/prabhu/work/MEDIA/m2/data/shuttle_flow_vel.vti', scene)
from enthought.mayavi.filters.extract_vector_norm import ExtractVectorNorm
extract_vector_norm = ExtractVectorNorm()
engine.add_filter(extract_vector_norm, vtkxml_file_reader1)
from enthought.mayavi.modules.streamline import Streamline
streamline = Streamline()
engine.add_filter(streamline, extract_vector_norm)
from enthought.mayavi.modules.outline import Outline
outline = Outline()
engine.add_filter(outline, extract_vector_norm)
scene.scene.camera.position = [-26.161739435640946, -23.33968605285963, -4.330818803012459]
scene.scene.camera.focal_point = [-0.30313491821289062, 0.0, 1.4027749300003052]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.41262625326967384, 0.24138827815138408, 0.87833437498696409]
scene.scene.camera.clipping_range = [12.567524761986057, 64.885104918139973]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-33.987476012111991, 7.0742035800218508, 9.2515505356797192]
scene.scene.camera.focal_point = [-0.30313491821289062, 0.0, 1.4027749300003052]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.27210126222372499, 0.27131677472862931, 0.92322700937911817]
scene.scene.camera.clipping_range = [13.498366440121661, 63.78023185599239]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
streamline.seed.widget.center = array([-1.76092294, -2.19636703, -4.07769924])
streamline.seed.widget.handle_direction = array([ 1.,  0.,  0.])
scene.scene.camera.position = [-0.14627247022011527, 35.246003093475835, -0.59149933326899151]
scene.scene.camera.focal_point = [-0.30313491821289062, 0.0, 1.4027749300003052]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.10775362069649223, 0.055684269920481991, 0.99261695497821301]
scene.scene.camera.clipping_range = [22.165106941458703, 51.720503614694223]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
streamline.seed.widget.center = array([-9.46036585, -1.98695846, -0.98230673])
streamline.seed.widget.handle_direction = array([ 1.,  0.,  0.])
scene.scene.camera.position = [-24.531837698557823, -25.223630761907124, -3.3952332503501701]
scene.scene.camera.focal_point = [-0.30313491821289062, 0.0, 1.4027749300003052]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.014255927708073379, -0.17361673895115709, 0.98471010783943314]
scene.scene.camera.clipping_range = [10.590545716157719, 65.485850871289045]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
# ------------------------------------------- 
from enthought.mayavi.tools.show import show
show()
