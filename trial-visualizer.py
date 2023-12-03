import pygame
import numpy as np
import pygame.locals as pg_locals
import librosa.display
import matplotlib.pyplot as plt
import io
import sys
import soundfile as sf

# Function to load audio file
def load_audio(file_path):
    y, sr = librosa.load(file_path)
    return y, sr

# Function to create a spectogram
def create_spectrogram(y, sr):
    plt.figure(figsize=(4, 4))
    plt.specgram(y, NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap='viridis', sides='default', mode='default', scale='dB')
    plt.axis('off')
    plt.savefig('spectrogram.png', bbox_inches='tight', pad_inches=0, transparent=True)
    plt.close()

# Function to play the audio
def play_audio(y, sr):
    sf.write('temp.wav', y, sr)
    pygame.mixer.init()
    pygame.mixer.music.load('temp.wav')
    pygame.mixer.music.play()

# Main function
def main(file_path):
    pygame.init()
    
    # Load audio file
    y, sr = load_audio(file_path)

    # Create a spectrogram
    create_spectrogram(y, sr)

    # Set up Pygame
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600), pg_locals.NOFRAME)
    bg = pygame.image.load('spectrogram.png')

    # Play audio
    play_audio(y, sr)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pg_locals.QUIT:
                running = False

        screen.blit(bg, (0, 0))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python visualizer.py <path_to_audio_file>")
    else:
        main(sys.argv[1])
