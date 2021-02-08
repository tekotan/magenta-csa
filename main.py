import note_seq
from note_seq.protobuf import music_pb2

from music_continuation import MusicContinue
from music_vae import MusicVae

def create_test_sequences():
    """
    Author: Akshit and Jenny
    Last Modified: 01/21/21

    Creating test music sequences
    """
    twinkle_twinkle = music_pb2.NoteSequence()

    # Add the notes to the sequence.
    twinkle_twinkle.notes.add(pitch=60, start_time=0.0, end_time=0.5, velocity=80)
    twinkle_twinkle.notes.add(pitch=60, start_time=0.5, end_time=1.0, velocity=80)
    twinkle_twinkle.notes.add(pitch=67, start_time=1.0, end_time=1.5, velocity=80)
    twinkle_twinkle.notes.add(pitch=67, start_time=1.5, end_time=2.0, velocity=80)
    twinkle_twinkle.notes.add(pitch=69, start_time=2.0, end_time=2.5, velocity=80)
    twinkle_twinkle.notes.add(pitch=69, start_time=2.5, end_time=3.0, velocity=80)
    twinkle_twinkle.notes.add(pitch=67, start_time=3.0, end_time=4.0, velocity=80)
    twinkle_twinkle.notes.add(pitch=65, start_time=4.0, end_time=4.5, velocity=80)
    twinkle_twinkle.notes.add(pitch=65, start_time=4.5, end_time=5.0, velocity=80)
    twinkle_twinkle.notes.add(pitch=64, start_time=5.0, end_time=5.5, velocity=80)
    twinkle_twinkle.notes.add(pitch=64, start_time=5.5, end_time=6.0, velocity=80)
    twinkle_twinkle.notes.add(pitch=62, start_time=6.0, end_time=6.5, velocity=80)
    twinkle_twinkle.notes.add(pitch=62, start_time=6.5, end_time=7.0, velocity=80)
    twinkle_twinkle.notes.add(pitch=60, start_time=7.0, end_time=8.0, velocity=80) 
    twinkle_twinkle.total_time = 8

    twinkle_twinkle.tempos.add(qpm=60)

    note_seq.plot_sequence(twinkle_twinkle)

    note_seq.play_sequence(twinkle_twinkle,synth=note_seq.fluidsynth)

    teapot = music_pb2.NoteSequence()
    teapot.notes.add(pitch=69, start_time=0, end_time=0.5, velocity=80)
    teapot.notes.add(pitch=71, start_time=0.5, end_time=1, velocity=80)
    teapot.notes.add(pitch=73, start_time=1, end_time=1.5, velocity=80)
    teapot.notes.add(pitch=74, start_time=1.5, end_time=2, velocity=80)
    teapot.notes.add(pitch=76, start_time=2, end_time=2.5, velocity=80)
    teapot.notes.add(pitch=81, start_time=3, end_time=4, velocity=80)
    teapot.notes.add(pitch=78, start_time=4, end_time=5, velocity=80)
    teapot.notes.add(pitch=81, start_time=5, end_time=6, velocity=80)
    teapot.notes.add(pitch=76, start_time=6, end_time=8, velocity=80)
    teapot.total_time = 8

    teapot.tempos.add(qpm=60)

    note_seq.plot_sequence(teapot)
    note_seq.play_sequence(teapot,synth=note_seq.synthesize)

    return twinkle_twinkle, teapot

if __name__ == '__main__':
    seq1, seq2 = create_test_sequences()
    music_continue = MusicContinue()
    music_vae = MusicVae()
    print("continuing twinkle twinkle")
    music_continue(seq1)
    print("generating 5 randomly generated music pieces")
    music_vae.generate(n=5)
    print("interpolating between twinkle twinkle and teapot in 8 steps")
    music_vae.interpolate(seq1, seq2)