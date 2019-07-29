
from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec
from export_spec import export_spec


def main():
    ns_builder = NWBNamespaceBuilder(doc='data type for holding power or phase spectra for a signal',
                                     name='ndx-spectrum',
                                     version='0.1.0',
                                     author='Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    Spectrum = NWBGroupSpec(
        neurodata_type_def='Spectrum',
        neurodata_type_inc='NWBDataInterface',
        doc='type for storing power or phase of spectrum')

    for data_name in ('power', 'phase'):
        Spectrum.add_dataset(
            name=data_name,
            doc='spectrum values',
            dims=(('frequency',), ('frequency', 'channel')),
            shape=((None,), (None, None)),
            dtype='float',
            quantity='?')

    Spectrum.add_dataset(name='frequencies',
                         doc='frequencies of spectrum',
                         dims=('frequency',),
                         shape=(None,),
                         dtype='float')

    Spectrum.add_link(target_type='TimeSeries',
                      doc='timeseries that this spectrum describes',
                      quantity='?',
                      name='source_timeseries')

    Spectrum.add_dataset(name='electrodes',
                         doc='the electrodes that this series was generated from',
                         neurodata_type_inc='DynamicTableRegion',
                         quantity='?')

    new_data_types = [Spectrum]

    ns_builder.include_type('NWBDataInterface', namespace='core')
    ns_builder.include_type('TimeSeries', namespace='core')

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
