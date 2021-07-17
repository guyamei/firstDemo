<template>
    <!--新增用例按钮，点击可以弹出编辑框，做新增-->
    <div>
      <template>
        <!--添加data-app="true"，解决vuetify bug-->
        <v-row justify="center" data-app="true">
          <v-dialog
            v-model="dialog"
            persistent
            max-width="600px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="primary"
                dark
                v-bind="attrs"
                v-on="on"
              >
                新增用例
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">新增用例</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        label="测试用例名称"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        label="测试步骤"
                        hint="example of helper text only on focus"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        label="备注"
                        hint="example of persistent helper text"
                        persistent-hint
                        required
                      ></v-text-field>
                    </v-col>
                    
                    
                    
                   
                  </v-row>
                </v-container>
                <small>*indicates required field</small>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="dialog = false"
                >
                  Close
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="addCase()"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-row>
      </template>
      <v-data-table :headers="headers" :items="desserts" :items-per-page="5" class="elevation-1">
      <template v-slot:item.operations="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil</v-icon>
        <v-icon small @click="deleteItem(item)" >mdi-delete</v-icon>
      </template>
      </v-data-table>
   </div>
</template>
<script>
  export default {
    data () {
      return {
        dialog: false,
        headers: [
          {
            text: '测试用例名称',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: '测试步骤', value: 'steps' },
          { text: '备注', value: 'description' },
          { text: '操作', value: 'operations' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            steps: 159,
            description: 6.0,
            operation: 24,
          },
          {
            name: 'Frozen Yogurt',
            steps: 159,
            description: 6.0,
            operation: 24,
          },
          {
            name: 'Frozen Yogurt',
            steps: 159,
            description: 6.0,
            operation: 24,
          },
        ],
      }
    },
    methods:{
      addCase: function()
      {
        this.$api.testcase.selectTestcase().then((result) => {
          console.log(result);
        })
        this.dialog = false;
      }
    }
  }
</script>
