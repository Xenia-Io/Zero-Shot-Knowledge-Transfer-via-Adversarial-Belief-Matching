import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, UpSampling2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LeakyReLU, Input, Reshape
from tensorflow.keras.layers import BatchNormalization
import tensorflow.keras.backend as K


class Generator():
    def __init__(self, args):
        self.batch_size = args.batch_size
        self.z_dim = args.z_dim

    def build_generator_model(self):
#         ip = Input(shape=(self.z_dim,))
        model = Sequential()
        n_nodes = 128 * 8 * 8
        model.add(Dense(n_nodes, input_dim = self.z_dim))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Reshape((8, 8, 128)))
        model.add(BatchNormalization(axis=-1))
        # upsample to 16x16 and convolve
        model.add(UpSampling2D(size=(2,2)))
        model.add(Conv2D(128, (3, 3), strides=(1, 1), padding='same'))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(axis=-1))
        # upsample to 32x32 and convolve
        model.add(UpSampling2D(size=(2,2)))
        model.add(Conv2D(64, (3, 3), strides=(1, 1), padding='same'))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(axis=-1))
        # output layer
        # Maybe a ReLU layer in?
        model.add(Conv2D(3, (3, 3), activation='relu', padding='same'))
        model.add(BatchNormalization(axis=-1))
        # model = Model(ip, x)

        return model


if __name__ == '__main__':
    args = type('', (), {})()
    args.batch_size = 128
    args.z_dim = 100
    print(args.batch_size)
    print(args.z_dim)
    generator_model = Generator(args)
    generator_model = generator_model.build_generator_model()

    generator_model.summary()
    