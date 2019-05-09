# -*- coding: utf-8 -*-
import argparse

# Logger definition
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

fh = logging.FileHandler(os.path.join(config.save_dir, "train.log"))
logger.addHandler(fh)

logger.info("Training starts ...")
