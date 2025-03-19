import numpy as np
def psk(digital_signal, baseband_amplitude, modulation_frequency, modulation_index=0.5, t=None):
    """
    Function to modulate a digital signal using Phase Shift Keying (PSK).

    Parameters:
    digital_signal (array-like): The digital signal to be modulated.
    baseband_amplitude (float): The amplitude of the baseband signal.
    modulation_frequency (float): The frequency of the modulation.
    modulation_index (float, optional): The modulation index. Default is 0.5.
    t (array-like, optional): Time vector for the modulation. If None, it will be generated.

    Returns:
    np.ndarray: The modulated PSK signal.
    """
    
    # Ensure the digital signal is a numpy array
    digital_signal = np.asarray(digital_signal)
    
    # Generate time vector if not provided
    if t is None:
        t = np.arange(len(digital_signal)) / len(digital_signal)
    
    # Calculate the phase shift based on the digital signal
    phase_shift = np.pi * modulation_index * digital_signal
    
    # Generate the PSK signal
    psk_signal = baseband_amplitude * np.cos(2 * np.pi * modulation_frequency * t + phase_shift)
    
    return psk_signal