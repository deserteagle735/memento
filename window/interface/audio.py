from interface.qt import *
import time
import datetime

def record_audio(parent, media_folder):

    dialog_record = QMessageBox(parent)
    dialog_record.setWindowTitle("Memento")
    dialog_record.setStyleSheet("font: 12pt \"SF Pro Display\";")
    #icon
    dialog_record.setIconPixmap(QPixmap(":/resource/media-record.png"))
    #button
    button_save = QPushButton("Lưu")
    button_cancel = QPushButton("Hủy")
    dialog_record.addButton(button_save, QMessageBox.AcceptRole)
    dialog_record.addButton(button_cancel, QMessageBox.RejectRole)
    dialog_record.setEscapeButton(button_cancel)
    dialog_record.setDefaultButton(button_save)

    #file name
    filename = str(datetime.datetime.today().timestamp()) + ".wav"

    #audio recorder
    audio_recorder = QAudioRecorder()
    audio_settings = QAudioEncoderSettings()
    audio_settings.setCodec("audio/x-raw, layout=(string)interleaved")
    audio_settings.setQuality(QMultimedia.HighQuality)
    audio_recorder.setContainerFormat("audio/x-wav")
    audio_recorder.setAudioSettings(audio_settings)
    audio_recorder.setOutputLocation(QUrl.fromLocalFile(os.path.join(media_folder,filename)))

    t = time.time()
    audio_recorder.record()
    QApplication.instance().processEvents()
    print("Recording...")
    while not dialog_record.clickedButton():
        txt ="Đang ghi âm...\nThời gian: %0.1f"
        dialog_record.setText(txt % (time.time() - t))
        dialog_record.show()
        QApplication.instance().processEvents()

    if dialog_record.clickedButton() == dialog_record.escapeButton():
        audio_recorder.stop()
        try:
            os.remove(os.path.join(media_folder,filename)) 
            print("Record discard")
            return ""
        except:
            print("file " + filename + " not found")   
    else:
        while time.time() - t < 1:
            time.sleep(0.25)
        audio_recorder.stop()
        print("Record succeedfully", filename)
        return filename

def play_audio(media_folder, filename):
    # player.setMedia(str(QUrl.fromLocalFile(os.path.join(media_folder, filename))))
    # player.play()
    #QSound.play("/home/deserteagle735/Desktop/PyQt-audio-record/test.wav")
    if filename == "" or filename == None:
        print("Filename parameter is null")
        return
        
    print("Playing record", filename)
    try:
        QSound.play(os.path.join(media_folder, filename))
    except QErrorMessage as e:
        print(str(e))
    #player.play()

player = QMediaPlayer()
    

