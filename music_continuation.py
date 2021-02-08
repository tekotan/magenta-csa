import magenta
import note_seq
import tensorflow
from note_seq.protobuf import music_pb2

from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.shared import sequence_generator_bundle
from note_seq.protobuf import generator_pb2
from note_seq.protobuf import music_pb2

class MusicContinue:
    """
    Author: Tanish and Jenny
    Last Modified: 02/01/21
    Class to wrap the sequence model from Magenta to continue music sequences
    """
    def __init__(self):
        """
        Loads and initializes the rnn
        """
        print('Downloading model bundle. This will take less than a minute...')
        note_seq.notebook_utils.download_bundle('basic_rnn.mag', './content/')

        # Initialize the model.
        print("Initializing Melody RNN...")
        bundle = sequence_generator_bundle.read_bundle_file('./content/basic_rnn.mag')
        generator_map = melody_rnn_sequence_generator.get_generator_map()
        self.melody_rnn = generator_map['basic_rnn'](checkpoint=None, bundle=bundle)
        self.melody_rnn.initialize()

        print('🎉 Done!')
    def __call__(self, input_sequence):
        """
        Continues a music sequence

        Args:
            input_sequence: initial sequence to continue
                type: NoteSequence object
        Returns:
            NotesSequence object of continued music
        """
        num_steps = 128 # shorter or longer sequences
        temperature = 1.0 # the higher the temperature the more random the sequence.

        # Set the start time to begin on the next step after the last note ends.
        last_end_time = (max(n.end_time for n in input_sequence.notes)
                        if input_sequence.notes else 0)
        qpm = input_sequence.tempos[0].qpm 
        seconds_per_step = 60.0 / qpm / melody_rnn.steps_per_quarter
        total_seconds = num_steps * seconds_per_step

        generator_options = generator_pb2.GeneratorOptions()
        generator_options.args['temperature'].float_value = temperature
        generator_options.generate_sections.add(
            start_time=last_end_time + seconds_per_step,
            end_time=total_seconds)

        # Ask the model to continue the sequence.
        sequence = self.melody_rnn.generate(input_sequence, generator_options)

        note_seq.play_sequence(sequence, synth=note_seq.fluidsynth)
        return sequence