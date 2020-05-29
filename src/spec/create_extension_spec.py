from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec, export_spec
import os


def main():
    ns_builder = NWBNamespaceBuilder(doc='data type for holding power or phase spectra for a signal',
                                     name='ndx-spectrum',
                                     version='0.2.2',
                                     author='Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    ns_builder.include_type('NWBDataInterface', namespace='core')
    ns_builder.include_type('TimeSeries', namespace='core')
    ns_builder.include_type('DynamicTableRegion', namespace='core')

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

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    main()
