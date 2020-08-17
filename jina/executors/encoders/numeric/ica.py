__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

from . import FitTransformEncoder


class FastICAEncoder(FitTransformEncoder):
    """
    :class:`FastICAEncoder` encodes data from an ndarray in size `B x T` into an ndarray in size `B x D`.

    .. note:: 
        :class:`FastICAEncoder` must be trained before calling ``encode()``.
    """

    def __init__(self, output_dim: int, num_features: int = None, whiten: bool = False, *args, **kwargs):
        """

        :param output_dim: the output size.
        :param num_features: the number of input features.  If ``num_features`` is None, then ``num_features`` is
            inferred from the data
        :param whiten: If whiten is false, the data is already considered to be whitened, and no whitening is performed.
        """
        super().__init__(*args, **kwargs)
        self.output_dim = output_dim
        self.whiten = whiten
        self.num_features = num_features
        self.is_trained = False
        self.model = None

    def post_init(self):
        if not self.model:
            from sklearn.decomposition import FastICA
            self.model = FastICA(
                n_components=self.output_dim,
                whiten=self.whiten)
