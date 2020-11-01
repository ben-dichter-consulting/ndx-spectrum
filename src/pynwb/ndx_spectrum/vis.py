import matplotlib.pyplot as plt
from collections.abc import Iterable
from h5py import Dataset


def _data_to_array(data):
    if isinstance(data, Dataset):
        return data[()]
    else:
        return data


def show_spectrum(spectrum):
    naxes = 0
    if 'power' in spectrum.fields:
        naxes += 1
    if 'phase' in spectrum.fields:
        naxes += 1

    fig, axs = plt.subplots(naxes, 1, sharex=True)

    caxes = 0
    if not isinstance(axs, Iterable):
        ax = [axs]
    for ax_ in ax:
        if 'power' in spectrum.fields:
            ax_.semilogy(_data_to_array(spectrum.frequencies), _data_to_array(spectrum.power))
            ax_.set_ylabel('Power')

            caxes += 1

        if 'phase' in spectrum.fields:
            ax_.plot(_data_to_array(spectrum.frequencies), _data_to_array(spectrum.phase))
            ax_.set_ylabel('phase')

        ax_.set_xlabel('frequency')

    return fig
