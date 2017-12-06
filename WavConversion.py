import sox
# create combiner
from Tools.i18n.pygettext import safe_eval

tfm = sox.Transformer()
# convert output to 8000 Hz stereo
tfm.convert(samplerate=8000,n_channels=1,bitdepth=8)

# create the output file.
tfm.build('C:/bin/HD1.wav', 'C:/bin/HD1_converted.wav')