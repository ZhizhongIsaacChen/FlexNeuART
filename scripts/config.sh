
# Point COLLECT_ROOT to the location you want to use as
# the root directory for all collections/indices.


COLLECT_ROOT="collections"

# The structure of sub-directories is outlined below

#
# Each collection is supposed to be stored in respective sub-directories.
# See a description/location of sub-directories below, which are assumed
# to exist (by many scripts).
#
# $COLLECT_ROOT
#     <Collection sub-directory>
#         $INPUT_RAW_SUBDIR (optional)
#         $INPUT_DATA_SUBDIR
#             $TRAIN_SUBDIR
#             $DEV_SUBDIR (optional)
#             $DEV1_SUBDIR (optional)
#             $DEV2_SUBDIR (optional)
#             $BITEXT_TRAIN_SUBDIR (optional, can also be created using
#                                   scripts/data_convert/split_train4bitext.sh
#                                   from the train subdir data)
#
#         $EXPER_DESC_SUBDIR
#         $EXPER_SUBDIR
#
#         $DERIVED_DATA_SUBDIR
#             $BITEXT_SUBDIR (optional)
#             $EMBED_SUBDIR (optional)
#             $LM_FINETUNE_SUBDIR (optional)
#
#         $FWD_INDEX_SUBDIR
#         $LUCENE_INDEX_SUBDIR
#         $LUCENE_CACHE_SUBDIR
#

# Original input data directory
INPUT_RAW_SUBDIR="input_raw"

# Processed multi-field input data (possibly compressed question and/or answer JSONs)
INPUT_DATA_SUBDIR="input_data"
# Derived data subdirectory
DERIVED_DATA_SUBDIR="derived_data"

# Experimental descriptors
EXPER_DESC_SUBDIR="exper_desc"
# This keeps data generated by experiments (results, models, etc)
EXPER_SUBDIR="results"

# Index directories.
FWD_INDEX_SUBDIR="forward_index"
LUCENE_INDEX_SUBDIR="lucene_index"

# By default training scripts cache candidate
# documents obtained from Lucene to speed up training
LUCENE_CACHE_SUBDIR="lucene_cache"

# Embeddings are stored within the derived-data sub-directory
EMBED_SUBDIR="embeddings"

# This is a bunch of sub-directories for input data
TRAIN_SUBDIR="train"
# The dev* directories can be optional, there can be, e.g., dev1, dev2 or just a single dev
DEV_SUBDIR="dev"
DEV1_SUBDIR="dev1"
DEV2_SUBDIR="dev2"
BITEXT_TRAIN_SUBDIR="train_bitext"

# A directory with data for BERT LM fine-tuning
LM_FINETUNE_SUBDIR="lm_finetune_data"
LM_FINETUNE_SET_PREF="set"

FEAT_EXPER_SUBDIR="$EXPER_SUBDIR/feat_exper"
FINAL_EXPER_SUBDIR="$EXPER_SUBDIR/final_exper"

# Parallel corpora sub-directory
BITEXT_SUBDIR="bitext"
# Parameters to train Model 1
GIZA_SUBDIR="giza"
GIZA_ITER_QTY=5

# Coordinate ascent (LETOR algorithm) training parameters
DEFAULT_METRIC_TYPE="NDCG@20"
DEFAULT_NUM_RAND_RESTART=10
DEFAULT_NUM_TREES=100

# QREL file name
QREL_FILE="qrels.txt"
# The default run id for TREC-like run files
FAKE_RUN_ID="fake_run"

# This value should match Lucene's query field
QUERY_FIELD_NAME=text


DEFAULT_TRAIN_CAND_QTY=20
DEFAULT_TEST_CAND_QTY_LIST=10,50,100,250