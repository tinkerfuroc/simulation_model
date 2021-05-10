#!/usr/bin/env python

import rospy
from moveit_msgs.msg import PlanningScene, PlanningSceneComponents, AllowedCollisionMatrix
from moveit_msgs.srv import GetPlanningScene

class AllowCollision(object):
    def __init__(self):
        self._pubPlanningScene = rospy.Publisher('/planning_scene', PlanningScene, queue_size=2)
        rospy.wait_for_service('/get_planning_scene', 10.0)

    def add_allowed_collision(self, str_id):
        get_planning_scene = rospy.ServiceProxy('/get_planning_scene', GetPlanningScene)
        request = PlanningSceneComponents(components=PlanningSceneComponents.ALLOWED_COLLISION_MATRIX)
        response = get_planning_scene(request)
        acm = response.scene.allowed_collision_matrix
        print(type(acm))
        if not str_id in acm.default_entry_names:
            acm.default_entry_names += [str_id]
            acm.default_entry_values += [True]
            print(acm)

            planning_scene_diff = PlanningScene(is_diff=True, allowed_collision_matrix=acm)
            self._pubPlanningScene.publish(planning_scene_diff)
            rospy.sleep(1.0)


if __name__ == '__main__':
    rospy.init_node('allowed_collision_handle', anonymous=False)
    ac = AllowCollision()
    ac.add_allowed_collision('object')
