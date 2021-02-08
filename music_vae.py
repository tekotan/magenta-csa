import magenta
import note_seq
import tensorflow
from note_seq.protobuf import music_pb2

from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel

class MusicVae:
    """
    Author: Tanish and Akshit
    Last Modified: 02/02/21
    Version: 1.2
    Class to wrap the music vae trained from magenta
    """
    def __init__(self):
        """
        Loads and initializes the vae
        """
        print("Initializing Music VAE...")
        self.music_vae = TrainedModel(
            configs.CONFIG_MAP['cat-mel_2bar_big'], 
            batch_size=4, 
            checkpoint_dir_or_path='/content/mel_2bar_big.ckpt')
        print('🎉 Done!')

    def generate(self, n=2, length=80, temperature=1.0):
        """
        Generates a random music sequence

        Args:
            n: number of samples to generate 
                type: int
            length: length of each sample
                type: int
            temperature: emphirical magnitude of randomness in generated sequences
                type: float
        Returns:
            List[NotesSequence] of generated music
        """
        generated_sequences = music_vae.sample(n=2, length=80, temperature=1.0)
        for ns in generated_sequences:
            note_seq.play_sequence(ns, synth=note_seq.fluidsynth)
        return generated_sequences
    def interpolate(self, sequence_one, sequence_two, num_steps=8):
        """
        Continues a music sequence

        Args:
            sequence_one: first sequence
                type: NoteSequence object
            sequence_two: second sequence
                type: NoteSequence object
            num_steps: number of sequences to interpolate through
                type: int
        Returns:
            NotesSequence object of interpolated music
        """
        # This gives us a list of sequences.
        note_sequences = self.music_vae.interpolate(
            twinkle_twinkle,
            teapot, 
            num_steps=num_steps,
            length=32)

        # Concatenate them into one long sequence, with the start and 
        # end sequences at each end. 
        interp_seq = note_seq.sequences_lib.concatenate_sequences(note_sequences)

        note_seq.play_sequence(interp_seq, synth=note_seq.fluidsynth)
        return interp_seq