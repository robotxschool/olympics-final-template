from gym_duckietown.tasks.task_solution import TaskSolution
import numpy as np
import cv2


class LfChallengeTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']
        obs, _, _, _ = env.step([0, 0])
        while True:
            for i in range(100):
                obs, _, _, _ = env.step([0.25, 0])
                # obs already in BGR
            for i in range(100):
                obs, _, _, _ = env.step([-0.25, 0])
                # obs already in BGR
            obs, _, _, _ = env.step([0, 0])
            break




