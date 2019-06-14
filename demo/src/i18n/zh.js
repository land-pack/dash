import chineseMessages from "ra-language-chinese";

export default {
  ...chineseMessages,
  pos: {
    search: "搜索",
    configuration: "配置",
    language: "语言",
    theme: {
      name: "主题",
      light: "亮",
      dark: "暗"
    },
    dashboard: {
      monthly_revenue: "月结算",
      new_orders: "新订单",
      pending_reviews: "待处理评论",
      new_customers: "新客户",
      pending_orders: "待处理订单",
      order: {
        items:
          "通过 %{customer_name}, 一个项目|||| 是 %{customer_name}, %{nb_items} 项目"
      },
      welcome: {
        title: "欢迎来到react 后台管理",
        subtitle: "这是一个xxx后台管理平台",
        aor_button: "react-admin site",
        demo_button: "Source for this demo"
      }
    },
    menu: {
      sales: "销售",
      catalog: "目录",
      customers: "客户"
    }
  },
  resources: {
    customers: {
      name: "客户 |||| 客户",
      fields: {
        commands: "订单",
        groups: "阶段",
        last_seen_gte: "最近的活动时间",
        name: "名字",
        total_spent: "总消费"
      },
      tabs: {
        identity: "标示",
        address: "地址",
        orders: "订单",
        reviews: "反馈",
        stats: "状态"
      },
      page: {
        delete: "删除用户"
      }
    },
    commands: {
      name: "Order |||| Orders",
      title: "Order %{reference}",
      fields: {
        basket: {
          delivery: "Delivery",
          reference: "Reference",
          quantity: "Quantity",
          sum: "Sum",
          tax_rate: "Tax Rate",
          total: "Total",
          unit_price: "Unit Price"
        },
        customer_id: "Customer",
        date_gte: "Passed Since",
        date_lte: "Passed Before",
        total_gte: "Min amount",
        status: "Status",
        returned: "Returned"
      }
    },
    invoices: {
      name: "Invoice |||| Invoices",
      fields: {
        date: "Invoice date",
        customer_id: "Customer",
        command_id: "Order",
        date_gte: "Passed Since",
        date_lte: "Passed Before",
        total_gte: "Min amount",
        address: "Address"
      }
    },
    products: {
      name: "Poster |||| Posters",
      fields: {
        category_id: "Category",
        height_gte: "Min height",
        height_lte: "Max height",
        height: "Height",
        image: "Image",
        price: "Price",
        reference: "Reference",
        stock_lte: "Low Stock",
        stock: "Stock",
        thumbnail: "Thumbnail",
        width_gte: "Min width",
        width_lte: "Max width",
        width: "Width"
      },
      tabs: {
        image: "Image",
        details: "Details",
        description: "Description",
        reviews: "Reviews"
      }
    },
    categories: {
      name: "Category |||| Categories",
      fields: {
        products: "Products"
      }
    },
    reviews: {
      name: "Review |||| Reviews",
      detail: "Review detail",
      fields: {
        customer_id: "Customer",
        command_id: "Order",
        product_id: "Product",
        date_gte: "Posted since",
        date_lte: "Posted before",
        date: "Date",
        comment: "Comment",
        rating: "Rating"
      },
      action: {
        accept: "Accept",
        reject: "Reject"
      },
      notification: {
        approved_success: "Review approved",
        approved_error: "Error: Review not approved",
        rejected_success: "Review rejected",
        rejected_error: "Error: Review not rejected"
      }
    },
    segments: {
      name: "Segments",
      fields: {
        customers: "Customers",
        name: "Name"
      },
      data: {
        compulsive: "Compulsive",
        collector: "Collector",
        ordered_once: "Ordered once",
        regular: "Regular",
        returns: "Returns",
        reviewer: "Reviewer"
      }
    }
  }
};
