<template>
  <div class="file-box">
    <Form enctype="multipart/form-data">
      <FormItem :style="{'width': '70%', 'margin': 'auto'}">
        <Upload
          action
          type="drag"
          :max-size="100"
          :format="['txt']"
          :on-exceeded-size="exceededSize"
          :before-upload="beforeUploadFile"
          :on-format-error="handleFormatError"
        >
          <div style="padding: 20px 0">
            <Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
            <p>点击或将文件拖拽到这里上传</p>
          </div>
        </Upload>
      </FormItem>
    </Form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      files: [],
      isUploadFile: false,
    };
  },
  watch: {
    isUploadFile: function(val) {
      if (val) {
        let reader = new FileReader();
        reader.readAsText(this.files[0], "utf-8");
        // reader.readAsBinaryString(this.files[0]);
        reader.onerror = function(e) {
          console.log("读取文件出错！");
        };
        reader.onload = function(e) {
          console.log("读文件结束");
        };
        reader.onloadend = e => {
          console.log("读文件成功");

          console.log("Files", this.files);
          console.log("FileReader", reader);

          this.$http
            .post(
              "/cgi-bin/uploadFiles.py",
              {
                file: reader.result,
                name: this.files[0].name,
                time: this.dateFormat(new Date())
              },
              {
                emulateJSON: true
              }
            )
            .then(resp => {
              console.log(resp);
              if (resp.data === "success") {
                this.$Message.success("上传成功");
              } else {
                this.$Message.error("上传失败");
              }
            })
            .catch(error => {
              console.log(error);
            });
        };
      }
    }
  },
  methods: {
    handleFormatError(file) {
      this.$Message.error('error')
      // this.$Notice.warning({
      //   title: "文件格式不正确",
      //   desc:
      //     "文件 " + file.name + " 格式不正确，请上传 txt 格式的文件。"
      // });
    },
    exceededSize(file) {
      this.$Message.error('error')
      // this.$Notice.warning({
      //   title: "超出文件大小限制",
      //   desc: "文件 " + file.name + " 太大，不能超过 100kb。"
      // });
    },
    beforeUploadFile(file) {
      this.files.push(file);
      this.isUploadFile = true;
      return false;
    },
    dateFormat: function(time) {
      var date = new Date(time);
      var year = date.getFullYear();
      /* 在日期格式中，月份是从0开始的，因此要加0
       * 使用三元表达式在小于10的前面加0，以达到格式统一  如 09:11:05
       * */
      var month =
        date.getMonth() + 1 < 10
          ? "0" + (date.getMonth() + 1)
          : date.getMonth() + 1;
      var day = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();
      var hours =
        date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
      var minutes =
        date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
      var seconds =
        date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();
      // 拼接
      return (
        year +
        "-" +
        month +
        "-" +
        day +
        " " +
        hours +
        ":" +
        minutes +
        ":" +
        seconds
      );
    }
  }
};
</script>

<style scoped>
.file-box {
  padding: 40px 20px;
}
</style>
