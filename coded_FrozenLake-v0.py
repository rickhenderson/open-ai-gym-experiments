# Basic Agent Class from Code samples on OpenGym
# Modified by Rick Henderson
# Modified on May 4, 2016
# May the 4th be with you!

import logging
import os

import gym

# The world's simplest agent!
class CodedAgent(object):
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        # Set some sort of action
        # UP = 0, RIGHT = 1, DOWN = 2, LEFT = 3
	move = 2

        # Return the action as an integer in the required range.
        return move

if __name__ == '__main__':
    # You can optionally set up the logger. Also fine to set the level
    # to logging.DEBUG or logging.WARN if you want to change the
    # amount of outut.
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    env = gym.make('FrozenLake-v0')
    agent = CodedAgent(env.action_space)
    
    # Action space is Discrete(4), values 0 - 3
    # UP = 0, RIGHT = 1, DOWN = 2, LEFT = 3

    # You provide the directory to write to (can be an existing
    # directory, but can't contain previous monitor results. You can
    # also dump to a tempdir if you'd like: tempfile.mkdtemp().
    outdir = "tmp/c2"
    env.monitor.start(outdir, force=True)

    episode_count = 100
    max_steps = 200
    reward = 0
    done = False

    for i in xrange(episode_count):
        ob = env.reset()
        reward = done = None

        for j in xrange(max_steps):
            action = agent.act(ob, reward, done)
            ob, reward, done, _ = env.step(action)
            env.render()
            if done:
                break

    # Dump result info to disk
    env.monitor.close()

    # Upload to the scoreboard. We could also do this from another
    # process if we wanted.
    logger.info("Successfully ran CodedAgent. Now trying to upload results to the scoreboard. If it breaks, you can always just try re-uploading the same results.")
    gym.upload(outdir, algorithm_id='coded', api_key='YOUR API_KEY')
