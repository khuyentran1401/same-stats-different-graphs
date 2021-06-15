from .same_stats import main
import argparse

parser = argparse.ArgumentParser(description='Turn one shape into another shape while still keeping the statistics')
parser.add_argument('--shape_start', type=str, help='Starting shape', required=True, choices=['dino', 'rando', 'slant', 'big_slant'])
parser.add_argument('--shape_end', type=str, help='Target shape', required=True, choices=['x', 'h_lines', 'v_lines', 'wide_lines', 'high_lines', 'slant_up', 'slant_down', 'center', 'star', 'down_parab', 'circle', 'bullseye', 'dots'])
parser.add_argument('--iters', type=int, help='Number of iteration')
parser.add_argument('--decimals', type=float, help='Number of decimals')
parser.add_argument('--frames', type=int, help='Number of frames')
args = parser.parse_args()

if args.shape_start:
    main(args)