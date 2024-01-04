GPU_NUM=1; \
python src/run.py --argoverse --argoverse2 --future_frame_num 60 \
  --do_train --data_dir /media/zetlin/Data2/Argoverse2/val  --output_dir ~/argoverse2 \
  --hidden_size 128 --train_batch_size 64 --use_map \
  --core_num 16 --use_centerline --distributed_training ${GPU_NUM} \
  --other_params semantic_lane \
    direction \
    l1_loss \
    goals_2D \
    enhance_global_graph \
    subdivide \
    goal_scoring \
    laneGCN \
    point_sub_graph \
    lane_scoring \
    complete_traj \
    complete_traj-3 