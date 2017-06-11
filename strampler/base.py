"""
Base stratified sampler class
"""

class Strampler(object):
    """Base Strampler class to be inherite

    :param num_classes: number of label classes
    """
    def __init__(self, num_classes):
        self.num_classes = num_classes

    def sample(self, label):
        """Get a sample from input

        :param label: the label class this sample belongs to
        """
        raise NotImplementedError

    def sample_batch(self, size):
        """Get a batch of samples

        :param size: number of samples in the batch
        """
        raise NotImplementedError

