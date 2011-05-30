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
scene.scene.camera.position = [-7.8710042803035831, -23.270734468965951, 26.848457084803901]
scene.scene.camera.focal_point = [-0.30313491821289062, 0.0, 1.4027749300003052]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.18791276028283388, 0.75198808427818908, 0.63182490899497246]
scene.scene.camera.clipping_range = [21.722908882245918, 52.482070417945934]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-29.36388986802725, -16.258291095191616, 13.125528963969458]
scene.scene.camera.focal_point = [-0.30313491821289062, 0.0, 1.4027749300003052]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.17522011839126639, 0.35024314762581926, 0.92012371323214404]
scene.scene.camera.clipping_range = [16.803351361631922, 58.674779759221536]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
surface.actor.property.edge_visibility = True
surface.actor.property.line_width = 1.1832000017166138
surface.actor.property.line_width = 1.1831999999999998
vtkxml_file_reader1 = engine.open(u'/Users/prabhu/work/MEDIA/m2/data/shuttle_flow_vel.vti', scene)
from enthought.mayavi.filters.extract_vector_norm import ExtractVectorNorm
extract_vector_norm = ExtractVectorNorm()
engine.add_filter(extract_vector_norm, vtkxml_file_reader1)
from enthought.mayavi.modules.streamline import Streamline
streamline = Streamline()
engine.add_filter(streamline, extract_vector_norm)
from enthought.mayavi.modules.outline import Outline
outline = Outline()
module_manager1 = extract_vector_norm.children[0]
engine.add_filter(outline, module_manager1)
scene.scene.camera.position = [-35.527291132838059, 1.5271766756373661, 3.1941487321866866]
scene.scene.camera.focal_point = [-0.30313491821289062, 0.0, 1.4027749300003052]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.061459962287939186, 0.30146804029963314, 0.9514934018233987]
scene.scene.camera.clipping_range = [16.205447930141609, 60.499114495812179]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
streamline.seed.widget.center = array([-0.25031545, -0.70449392, -2.82145082])
streamline.seed.widget.handle_direction = array([ 1.,  0.,  0.])
scene.scene.camera.position = [-18.768485102212434, -27.67378446387562, 13.212726909551698]
scene.scene.camera.focal_point = [-0.30313491821289062, 0.0, 1.4027749300003052]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.43630018818630739, 0.090909067630530527, 0.89519701027826293]
scene.scene.camera.clipping_range = [12.911509899232243, 64.852594297042543]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
streamline.seed.widget.center = array([-4.35750409,  1.91665121, -3.10118704])
streamline.seed.widget.handle_direction = array([ 1.,  0.,  0.])
streamline.seed.widget.center = array([-4.35750409,  1.91665121, -3.10118704])
streamline.seed.widget.handle_direction = array([ 1.,  0.,  0.])
# ------------------------------------------- 
from enthought.mayavi.tools.show import show
show()
