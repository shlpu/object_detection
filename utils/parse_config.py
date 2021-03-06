import yaml


class DataConfig(yaml.YAMLObject):
    yaml_tag = u'!data'

    def __init__(self,
                 n_items_min=1,
                 n_items_max=3):
        self.n_items_min = n_items_min
        self.n_items_max = n_items_max

    def __repr__(self):
        return 'data_config'


class TrainConfig(yaml.YAMLObject):
    yaml_tag = u'!train'

    def __init__(self,
                 is_training=False,
                 model_dir=None,
                 shuffle=True,
                 filenames_shuffle_buffer_size=100,
                 num_parallel_map_calls=2,
                 num_epochs=0,
                 num_readers=32,
                 read_block_length=32,
                 shuffle_buffer_size=2048,
                 prefetch_size=512,
                 batch_size=2,
                 learning_rate=0.001,
                 learning_rate_decay=None,
                 optimizer=None,
                 bbox_clf_weight=1.,
                 bbox_reg_weight=1.,
                 quantize=False):
        self.is_training = is_training
        if model_dir is None:
            model_dir = './models'
        self.model_dir = model_dir
        self.shuffle = shuffle
        self.filenames_shuffle_buffer_size = filenames_shuffle_buffer_size
        self.num_parallel_map_calls = num_parallel_map_calls
        self.num_epochs = num_epochs
        self.num_readers = num_readers
        self.read_block_length = read_block_length
        self.shuffle_buffer_size = shuffle_buffer_size
        self.prefetch_size = prefetch_size
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.learning_rate_decay = learning_rate_decay
        if optimizer is None:
            optimizer = {'name': 'adam'}
        self.optimizer = optimizer
        self.bbox_clf_weight = bbox_clf_weight
        self.bbox_reg_weight = bbox_reg_weight
        self.quantize = quantize

    def __repr__(self):
        return 'train_config'


class ModelConfig(yaml.YAMLObject):
    yaml_tag = u'!model'

    def __init__(self,
                 model_name=None,
                 input_shape=None,
                 output_shape=None,
                 output_stride=8,
                 depth_multiplier=1.,
                 min_depth=8,
                 backbone_endpoint=None,
                 final_depth=96,
                 base_anchor_sizes=None,
                 base_anchor_strides=None,
                 anchor_scales=None,
                 anchor_ratios=None,
                 unmatched_threshold=0.4,
                 matched_threshold=0.7,
                 force_match_for_gt_bbox=True,
                 scale_factors=None):
        self.model_name = model_name
        if input_shape is None:
            input_shape = [224, 224]
        if output_shape is None:
            output_shape = input_shape
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.output_stride = output_stride
        self.depth_multiplier = depth_multiplier
        self.min_depth = min_depth
        self.backbone_endpoint = backbone_endpoint
        self.final_depth = final_depth
        self.base_anchor_sizes = base_anchor_sizes
        self.base_anchor_strides = base_anchor_strides
        self.anchor_ratios = anchor_ratios
        self.anchor_scales = anchor_scales
        self.unmatched_threshold = unmatched_threshold
        self.matched_threshold = matched_threshold
        self.force_match_for_gt_bbox = force_match_for_gt_bbox
        if scale_factors is None:
            scale_factors = [10., 5.]
        self.scale_factors = scale_factors

    def __repr__(self):
        return 'model_config'


class InferConfig(yaml.YAMLObject):
    yaml_tag = u'!infer'

    def __init__(self,
                 model_dir=None,
                 frozen_model=None,
                 network_input_shape=None,
                 out_stride=8,
                 resize_shape=None,
                 strides=None,
                 input_type=None,
                 images=None,
                 video=None,
                 camera=None,
                 display_bbox=False):
        self.model_dir = model_dir
        self.frozen_model = frozen_model
        self.network_input_shape = network_input_shape
        self.out_stride = out_stride
        self.resize_shape = resize_shape
        self.strides = strides
        self.input_type = input_type
        self.images = images
        self.video = video
        self.camera = camera
        self.display_bbox = display_bbox

    def __repr__(self):
        return 'infer_config'


def parse_config(config_file):
    cfgs = {}
    with open(config_file, 'r') as f:
        for cfg in yaml.load_all(f):
            cfgs[str(cfg)] = cfg
    return cfgs
