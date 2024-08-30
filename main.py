def model():
    import tensorflow as tf
    from tensorflow.keras.applications import EfficientNetB1
    from tensorflow.keras.models import Model
    from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
    from tensorflow.keras.optimizers import Adam
    from tensorflow.keras.preprocessing.image import ImageDataGenerator


   

    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
        except RuntimeError as e:
            print(e)

    BatchSize = 4
    LearningRate =0.01
    EPOCHS = 2
    n_classes = 101

    base_model = EfficientNetB1(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

    x = base_model.output
    x = GlobalAveragePooling2D()(x)

    predictions = Dense(n_classes, activation='softmax')(x)

    model = Model(inputs=base_model.input, outputs=predictions)

    model.compile(optimizer=Adam(learning_rate=LearningRate), loss='categorical_crossentropy', metrics=['accuracy'])

    train_datagen = ImageDataGenerator(preprocessing_function=tf.keras.applications.efficientnet.preprocess_input, validation_split=0.3)
    train_generator = train_datagen.flow_from_directory(
        r'food-101/food-101/images',
        target_size=(224, 224),
        batch_size=BatchSize,
        class_mode='categorical',
        subset='training')

    validation_generator = train_datagen.flow_from_directory(
        r'food-101/food-101/images',
        target_size=(224, 224),
        batch_size=BatchSize,
        class_mode='categorical',
        subset='validation')

    model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // BatchSize,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // BatchSize,
        epochs=EPOCHS)

    model.save("food-image-recognition.h5")

if __name__ == '__main__':
    # if "/meow.h5":

    # #  print("yes")
    # return
    # else:
     model()
